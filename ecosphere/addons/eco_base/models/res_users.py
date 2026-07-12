from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    total_xp = fields.Integer(string='Total XP', default=0)
    current_rank = fields.Char(string='Current Rank', default='Novice')
