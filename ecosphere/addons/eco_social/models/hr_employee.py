from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    total_volunteer_hours = fields.Float(
        string='Total Volunteer Hours', 
        compute='_compute_total_volunteer_hours', 
        store=True,
        tracking=True
    )
    
    participation_ids = fields.One2many('eco.employee.participation', 'employee_id', string='CSR Participations')
    training_completion_ids = fields.One2many('eco.social.training.completion', 'employee_id', string='Training Completions')

    @api.depends('participation_ids.status', 'participation_ids.hours_credited')
    def _compute_total_volunteer_hours(self):
        for employee in self:
            approved = employee.participation_ids.filtered(lambda p: p.status == 'approved')
            employee.total_volunteer_hours = sum(approved.mapped('hours_credited'))
