from odoo import models, fields

class EcoCategory(models.Model):
    _name = 'eco.category'
    _description = 'EcoSphere Category'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    type = fields.Selection([
        ('csr', 'CSR'),
        ('challenge', 'Challenge'),
        ('reward', 'Reward'),
        ('policy', 'Policy'),
        ('audit', 'Audit'),
        ('compliance', 'Compliance')
    ], string='Type', required=True, tracking=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('archived', 'Archived')
    ], string='Status', default='active', tracking=True)
    color = fields.Integer(string='Color')
