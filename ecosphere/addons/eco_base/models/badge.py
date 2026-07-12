from odoo import models, fields

class EcoBadge(models.Model):
    _name = 'eco.badge'
    _description = 'EcoSphere Badge'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    icon = fields.Binary(string='Icon')
    xp_required = fields.Integer(string='XP Required', default=0, tracking=True)
    challenge_required = fields.Boolean(string='Challenge Required', default=False)
    status = fields.Selection([
        ('active', 'Active'),
        ('archived', 'Archived')
    ], string='Status', default='active', tracking=True)
