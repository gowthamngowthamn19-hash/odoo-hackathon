from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EmissionFactor(models.Model):
    _name = 'eco.emission.factor'
    _description = 'Emission Factor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True, help="e.g., Electricity, Diesel, Petrol")
    category = fields.Selection([
        ('energy', 'Energy'),
        ('transport', 'Transport'),
        ('waste', 'Waste'),
        ('material', 'Material'),
        ('other', 'Other')
    ], string='Category', required=True, tracking=True)
    unit = fields.Char(string='Unit', required=True, help="e.g., kWh, Liters, kg")
    factor = fields.Float(
        string='Factor (CO2e)', 
        required=True, 
        digits=(12, 6), 
        tracking=True, 
        help="CO2 equivalent emission per unit"
    )
    source = fields.Char(string='Source', tracking=True, help="Source of the emission factor data (e.g., EPA, DEFRA)")
    effective_date = fields.Date(
        string='Effective Date', 
        default=fields.Date.context_today, 
        required=True, 
        tracking=True
    )
    active = fields.Boolean(string='Active', default=True, tracking=True)

    @api.constrains('factor')
    def _check_factor_positive(self):
        for record in self:
            if record.factor <= 0:
                raise ValidationError(_("Emission factor must be strictly positive."))

    @api.constrains('name', 'unit', 'active')
    def _check_unique_active_factor(self):
        for record in self:
            if record.active:
                domain = [
                    ('name', '=', record.name),
                    ('unit', '=', record.unit),
                    ('active', '=', True),
                    ('id', '!=', record.id)
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(_("Only one active factor per activity and unit combination is allowed."))
