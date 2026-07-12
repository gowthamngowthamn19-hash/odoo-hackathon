from odoo import models, fields, api, _

class EcoChallenge(models.Model):
    _name = 'eco.challenge'
    _description = 'ESG Challenge'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(string='Title', required=True, tracking=True)
    category_id = fields.Many2one('eco.category', string='Category', tracking=True)
    department_id = fields.Many2one('hr.department', string='Department (Optional)', help="If set, only this department can join.")
    description = fields.Text(string='Description', tracking=True)
    difficulty = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('expert', 'Expert')
    ], string='Difficulty', default='easy', tracking=True)
    
    xp_reward = fields.Integer(string='XP Reward', default=50, required=True, tracking=True)
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    
    evidence_required = fields.Boolean(string='Evidence Required', default=True, tracking=True)
    maximum_participants = fields.Integer(string='Max Participants', default=0, help="0 means unlimited.")
    
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)
    approved_by = fields.Many2one('res.users', string='Approved By', readonly=True)
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('active', 'Active'),
        ('under_review', 'Under Review'),
        ('completed', 'Completed'),
        ('archived', 'Archived')
    ], string='Status', default='draft', tracking=True)

    def action_publish(self):
        self.write({'status': 'published'})
        return True

    def action_start(self):
        self.write({'status': 'active'})
        if 'eco.event.bus' in self.env:
            for record in self:
                self.env['eco.event.bus'].publish('challenge.active', {'challenge_id': record.id, 'title': record.title})
        return True

    def action_review(self):
        self.write({'status': 'under_review'})
        return True

    def action_complete(self):
        self.write({'status': 'completed'})
        return True

    def action_archive(self):
        self.write({'status': 'archived'})
        return True
