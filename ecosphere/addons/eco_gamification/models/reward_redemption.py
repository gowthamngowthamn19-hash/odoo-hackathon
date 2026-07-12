from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class RewardRedemption(models.Model):
    _name = 'eco.reward.redemption'
    _description = 'Reward Redemption Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    reward_id = fields.Many2one('eco.reward', string='Reward', required=True, tracking=True)
    points_used = fields.Integer(string='Points Used', readonly=True, tracking=True)
    
    requested_date = fields.Datetime(string='Requested Date', default=fields.Datetime.now, readonly=True)
    approved_by = fields.Many2one('res.users', string='Approved By', readonly=True)
    approved_date = fields.Datetime(string='Approved Date', readonly=True)
    
    status = fields.Selection([
        ('requested', 'Requested'),
        ('approved', 'Approved'),
        ('redeemed', 'Redeemed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='requested', tracking=True)

    @api.constrains('employee_id', 'reward_id')
    def _check_eligibility(self):
        for record in self:
            if record.reward_id.stock <= 0:
                raise ValidationError(_("This reward is out of stock."))
            
            current_xp = self.env['eco.gamification.engine'].get_employee_xp(record.employee_id)
            if current_xp < record.reward_id.points_required:
                raise ValidationError(_("You do not have enough XP to redeem this reward."))

    def action_approve(self):
        for record in self:
            record.points_used = record.reward_id.points_required
            record.reward_id.stock -= 1
            
        self.write({
            'status': 'approved',
            'approved_by': self.env.user.id,
            'approved_date': fields.Datetime.now()
        })
        
        # Emit Event for negative XP (redemption)
        if 'eco.event.bus' in self.env:
            for record in self:
                self.env['eco.event.bus'].publish('gamification.event', {
                    'event_code': 'REWARD_REDEEMED',
                    'event_name': f"Redeemed Reward: {record.reward_id.name}",
                    'employee_id': record.employee_id.id,
                    'reference_model': 'eco.reward.redemption',
                    'reference_id': record.id,
                    'fallback_xp': -record.points_used
                })

    def action_redeem(self):
        self.write({'status': 'redeemed'})

    def action_cancel(self):
        for record in self:
            if record.status in ('approved', 'redeemed'):
                if 'eco.event.bus' in self.env:
                    self.env['eco.event.bus'].publish('gamification.event', {
                        'event_code': 'REWARD_REFUNDED',
                        'event_name': f"Cancelled Reward Refund: {record.reward_id.name}",
                        'employee_id': record.employee_id.id,
                        'reference_model': 'eco.reward.redemption',
                        'reference_id': record.id,
                        'fallback_xp': record.points_used
                    })
                record.reward_id.stock += 1
        self.write({'status': 'cancelled'})
