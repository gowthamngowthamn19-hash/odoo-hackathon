from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ChallengeParticipation(models.Model):
    _name = 'eco.challenge.participation'
    _description = 'Challenge Participation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    challenge_id = fields.Many2one('eco.challenge', string='Challenge', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    joined_date = fields.Datetime(string='Joined Date', default=fields.Datetime.now, readonly=True)
    
    progress = fields.Float(string='Progress (%)', default=0.0, tracking=True)
    proof_attachment = fields.Binary(string='Proof Attachment')
    proof_notes = fields.Text(string='Proof Notes', tracking=True)
    submitted_date = fields.Datetime(string='Submitted Date', readonly=True)
    
    reviewed_by = fields.Many2one('res.users', string='Reviewed By', readonly=True)
    reviewed_date = fields.Datetime(string='Reviewed Date', readonly=True)
    
    xp_awarded = fields.Integer(string='XP Awarded', readonly=True)
    completion_percentage = fields.Float(string='Completion (%)', related='progress')
    
    status = fields.Selection([
        ('joined', 'Joined'),
        ('in_progress', 'In Progress'),
        ('proof_submitted', 'Proof Submitted'),
        ('approved', 'Approved'),
        ('completed', 'Completed')
    ], string='Status', default='joined', tracking=True)

    @api.constrains('challenge_id', 'employee_id')
    def _check_unique_participation(self):
        for record in self:
            count = self.search_count([
                ('challenge_id', '=', record.challenge_id.id),
                ('employee_id', '=', record.employee_id.id),
                ('id', '!=', record.id)
            ])
            if count > 0:
                raise ValidationError(_("An employee cannot join the same challenge twice."))

    def action_in_progress(self):
        self.write({'status': 'in_progress'})
        return True

    def action_submit_proof(self):
        for record in self:
            if record.challenge_id.evidence_required and not record.proof_attachment:
                raise ValidationError(_("Proof of evidence is mandatory for this challenge."))
        self.write({
            'status': 'proof_submitted',
            'submitted_date': fields.Datetime.now()
        })
        return True

    def action_approve(self):
        self.write({
            'status': 'approved',
            'reviewed_by': self.env.user.id,
            'reviewed_date': fields.Datetime.now()
        })
        
        # Create Gamification Event and process it immediately
        if 'eco.gamification.event' in self.env:
            for record in self:
                event = self.env['eco.gamification.event'].create({
                    'event_code': 'CHALLENGE_COMPLETED',
                    'event_name': f"Completed Challenge: {record.challenge_id.title}",
                    'employee_id': record.employee_id.id,
                    'reference_model': 'eco.challenge.participation',
                    'reference_id': record.id,
                    'metadata': {'fallback_xp': record.challenge_id.xp_reward}
                })
                # Process the event to generate XP transaction
                if 'eco.event.processor' in self.env:
                    self.env['eco.event.processor']._process_event(event)
        
        self.write({'status': 'completed'})
        return True
