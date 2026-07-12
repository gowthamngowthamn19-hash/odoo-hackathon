from odoo import models, fields

class XpRule(models.Model):
    _name = 'eco.xp.rule'
    _description = 'XP Rule Configuration'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    action_name = fields.Char(string='Action Name', required=True, tracking=True)
    action_code = fields.Char(string='Action Code', required=True, tracking=True, help="Unique code used by engine (e.g., 'csr_completed')")
    xp_value = fields.Integer(string='XP Value', required=True, default=0, tracking=True)
    enabled = fields.Boolean(string='Enabled', default=True, tracking=True)

    _sql_constraints = [
        ('unique_action_code', 'unique(action_code)', 'Action Code must be unique!')
    ]
