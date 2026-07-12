from odoo import models, fields, api, _

class EmployeeParticipation(models.Model):
    _name = 'eco.employee.participation'
    _description = 'Employee Participation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    department_id = fields.Many2one('hr.department', related='employee_id.department_id', store=True, string="Department")
    activity_id = fields.Many2one('eco.csr.activity', string='CSR Activity', required=True, tracking=True)
    
    status = fields.Selection([
        ('joined', 'Joined'),
        ('proof_submitted', 'Proof Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='joined', tracking=True)
    
    proof_attachment = fields.Binary(string='Proof of Participation')
    hours_credited = fields.Float(string='Hours Credited', tracking=True, readonly=True)

    def action_submit_proof(self):
        for record in self:
            record.status = 'proof_submitted'
        return True

    def action_approve(self):
        departments = self.env['hr.department']
        employees = self.env['hr.employee']
        for record in self:
            record.status = 'approved'
            record.hours_credited = record.activity_id.volunteer_hours_awarded
            if record.department_id:
                departments |= record.department_id
            employees |= record.employee_id
            
        # Centralized score updates
        for dept in departments.sudo():
            self.env['eco.social.score.engine'].update_department_social_metrics(dept)
        for emp in employees.sudo():
            emp._compute_total_volunteer_hours()
        return True

    def action_reject(self):
        for record in self:
            record.status = 'rejected'
            record.hours_credited = 0.0
        return True
