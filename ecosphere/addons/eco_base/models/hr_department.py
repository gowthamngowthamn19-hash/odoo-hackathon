from odoo import models, fields, api

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    environment_score = fields.Float(string='Environment Score', default=0.0, tracking=True)
    social_score = fields.Float(string='Social Score', default=0.0, tracking=True)
    governance_score = fields.Float(string='Governance Score', default=0.0, tracking=True)
    overall_score = fields.Float(string='Overall ESG Score', compute='_compute_overall_score', store=True)

    @api.depends('environment_score', 'social_score', 'governance_score')
    def _compute_overall_score(self):
        for record in self:
            record.overall_score = (record.environment_score + record.social_score + record.governance_score) / 3.0
