from odoo import models, fields, api

class GamificationEvent(models.Model):
    _name = 'eco.gamification.event'
    _description = 'Gamification Event Log'
    _order = 'created_date desc, id desc'

    event_code = fields.Char(string='Event Code', required=True, index=True)
    event_name = fields.Char(string='Event Name')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, index=True)
    department_id = fields.Many2one('hr.department', string='Department', related='employee_id.department_id', store=True)
    
    reference_model = fields.Char(string='Reference Model', required=True)
    reference_id = fields.Integer(string='Reference ID', required=True)
    metadata = fields.Json(string='Metadata', help='Additional event data in JSON format')
    
    status = fields.Selection([
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('failed', 'Failed')
    ], string='Status', default='pending', required=True, index=True)
    
    processed_date = fields.Datetime(string='Processed Date', readonly=True)
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now, required=True, readonly=True)

    def write(self, vals):
        return super().write(vals)
