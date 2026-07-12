from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    volunteer_hours = fields.Float(string='Volunteer Hours', default=0.0, tracking=True)
    carbon_saved = fields.Float(string='Carbon Saved (kg)', default=0.0, tracking=True)
    esg_points = fields.Integer(string='ESG Points', default=0, tracking=True)
    
    badge_count = fields.Integer(string='Badge Count', compute='_compute_badge_count')
    reward_count = fields.Integer(string='Reward Count', compute='_compute_reward_count')

    def _compute_badge_count(self):
        for record in self:
            # Placeholder: will be expanded in eco_gamification
            record.badge_count = 0

    def _compute_reward_count(self):
        for record in self:
            # Placeholder: will be expanded in eco_gamification
            record.reward_count = 0
