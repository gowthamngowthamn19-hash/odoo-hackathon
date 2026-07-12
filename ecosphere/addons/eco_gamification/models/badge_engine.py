from odoo import models, fields, api

class EmployeeBadge(models.Model):
    _name = 'eco.employee.badge'
    _description = 'Employee Badge Assignment'
    _order = 'date_awarded desc'
    
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    badge_id = fields.Many2one('eco.badge', string='Badge', required=True)
    date_awarded = fields.Datetime(string='Date Awarded', default=fields.Datetime.now, required=True, readonly=True)

class BadgeEngine(models.AbstractModel):
    _name = 'eco.badge.engine'
    _description = 'Badge Awarding Engine'

    @api.model
    def check_and_award_badges(self, employee):
        """ Checks eligibility against all active badges and awards them if not already earned. """
        active_badges = self.env['eco.badge'].search([('status', '=', 'active')])
        employee_badges = self.env['eco.employee.badge'].search([('employee_id', '=', employee.id)]).mapped('badge_id')
        
        current_xp = self.env['eco.gamification.engine'].get_employee_xp(employee)
        completed_challenges = self.env['eco.challenge.participation'].search_count([
            ('employee_id', '=', employee.id),
            ('status', '=', 'completed')
        ])
        
        for badge in active_badges:
            if badge in employee_badges:
                continue
                
            eligible = True
            if badge.xp_required > 0 and current_xp < badge.xp_required:
                eligible = False
            if badge.challenge_required and completed_challenges == 0:
                eligible = False
                
            if eligible:
                self.env['eco.employee.badge'].create({
                    'employee_id': employee.id,
                    'badge_id': badge.id
                })
