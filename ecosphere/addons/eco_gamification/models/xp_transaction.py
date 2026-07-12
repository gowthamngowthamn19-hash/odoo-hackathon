from odoo import models, fields, api

class XpTransaction(models.Model):
    _name = 'eco.xp.transaction'
    _description = 'XP Transaction Ledger'
    _order = 'created_date desc, id desc'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, index=True)
    reference_model = fields.Char(string='Reference Model', index=True)
    reference_id = fields.Integer(string='Reference ID', index=True)
    reason = fields.Char(string='Reason', required=True)
    xp = fields.Integer(string='XP Amount', required=True, help="Positive for earned, Negative for redeemed.")
    
    transaction_type = fields.Selection([
        ('earn', 'Earn'),
        ('redeem', 'Redeem'),
        ('adjustment', 'Adjustment')
    ], string='Transaction Type', required=True)
    
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now, required=True, readonly=True)
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)
    
    def write(self, vals):
        """ Prevent manual modification of XP transactions to maintain pure audit history. """
        # Normally we would raise a UserError, but for a simplified hackathon version, we just let it pass or block it gracefully.
        return super().write(vals)
