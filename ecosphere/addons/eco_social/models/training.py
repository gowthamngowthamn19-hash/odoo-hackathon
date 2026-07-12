from odoo import models, fields, api

class SocialTraining(models.Model):
    _name = 'eco.social.training'
    _description = 'ESG Social Training'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Training Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    category = fields.Selection([
        ('ethics', 'Ethics & Compliance'),
        ('dei', 'Diversity, Equity & Inclusion'),
        ('safety', 'Health & Safety'),
        ('wellbeing', 'Employee Well-being')
    ], string='Category', required=True, tracking=True)
    active = fields.Boolean(default=True)


class SocialTrainingCompletion(models.Model):
    _name = 'eco.social.training.completion'
    _description = 'Training Completion'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    department_id = fields.Many2one('hr.department', related='employee_id.department_id', store=True, string="Department")
    training_id = fields.Many2one('eco.social.training', string='Training Program', required=True, tracking=True)
    completion_date = fields.Date(string='Completion Date', default=fields.Date.context_today, required=True, tracking=True)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('verified', 'Verified')
    ], string='Status', default='draft', tracking=True)

    def action_verify(self):
        departments = self.env['hr.department']
        for record in self:
            record.status = 'verified'
            if record.department_id:
                departments |= record.department_id
                
        for dept in departments:
            self.env['eco.social.score.engine'].update_department_social_metrics(dept)
