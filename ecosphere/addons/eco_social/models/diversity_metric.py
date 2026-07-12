from odoo import models, fields, api

class DiversityMetric(models.Model):
    _name = 'eco.diversity.metric'
    _description = 'Diversity Metric Snapshot'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    department_id = fields.Many2one('hr.department', string='Department', required=True, tracking=True)
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True, tracking=True)
    
    female_ratio = fields.Float(string='Female Ratio (%)', help="Percentage of female employees in the department.", tracking=True)
    minority_ratio = fields.Float(string='Minority Ratio (%)', help="Percentage of minority employees.", tracking=True)
    disability_ratio = fields.Float(string='Disability Ratio (%)', help="Percentage of employees with disabilities.", tracking=True)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed')
    ], string='Status', default='draft', tracking=True)

    def action_confirm(self):
        departments = self.env['hr.department']
        for record in self:
            record.status = 'confirmed'
            departments |= record.department_id
            
        for dept in departments:
            self.env['eco.social.score.engine'].update_department_social_metrics(dept)
