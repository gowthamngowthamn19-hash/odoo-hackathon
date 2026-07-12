from odoo import models, fields

class EcoReward(models.Model):
    _name = 'eco.reward'
    _description = 'EcoSphere Reward'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    points_required = fields.Integer(string='Points Required', default=0, tracking=True)
    stock = fields.Integer(string='Stock', default=0, tracking=True)
    image = fields.Binary(string='Image')
    status = fields.Selection([
        ('active', 'Active'),
        ('archived', 'Archived')
    ], string='Status', default='active', tracking=True)
