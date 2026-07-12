from odoo import models, fields, api, _

class CsrActivity(models.Model):
    _name = 'eco.csr.activity'
    _description = 'CSR Activity'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Activity Name', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    location = fields.Char(string='Location', tracking=True)
    
    reward_points = fields.Integer(string='Reward Points', default=0, help="Points awarded for gamification (if installed).", tracking=True)
    volunteer_hours_awarded = fields.Float(string='Volunteer Hours', default=0.0, required=True, help="Hours credited to employee upon completion.", tracking=True)
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('archived', 'Archived')
    ], string='Status', default='draft', tracking=True)

    def action_publish(self):
        for record in self:
            record.status = 'published'

    def action_start(self):
        for record in self:
            record.status = 'active'

    def action_complete(self):
        for record in self:
            record.status = 'completed'

    def action_archive(self):
        for record in self:
            record.status = 'archived'

    def action_draft(self):
        for record in self:
            record.status = 'draft'
