from odoo import models, fields

class HrEmployeeGamification(models.Model):
    _inherit = 'hr.employee'

    challenge_participation_ids = fields.One2many('eco.challenge.participation', 'employee_id', string='Challenges')
    earned_badge_ids = fields.One2many('eco.employee.badge', 'employee_id', string='Badges')
    xp_transaction_ids = fields.One2many('eco.xp.transaction', 'employee_id', string='XP History')
    reward_redemption_ids = fields.One2many('eco.reward.redemption', 'employee_id', string='Redeemed Rewards')
    
    current_xp = fields.Integer(string='Current XP', compute='_compute_gamification_stats')
    current_rank = fields.Integer(string='Rank', compute='_compute_gamification_stats')
    
    def _compute_gamification_stats(self):
        for record in self:
            record.current_xp = self.env['eco.gamification.engine'].get_employee_xp(record)
            leaderboard_entry = self.env['eco.leaderboard'].search([('employee_id', '=', record.id)], limit=1)
            record.current_rank = leaderboard_entry.rank if leaderboard_entry else 0
