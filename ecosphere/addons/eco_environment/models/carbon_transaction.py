from odoo import models, fields, api, _

class CarbonTransaction(models.Model):
    _name = 'eco.carbon.transaction'
    _description = 'Carbon Transaction'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'

    reference = fields.Char(string='Reference', required=True, copy=False, tracking=True, default=lambda self: _('New'))
    department_id = fields.Many2one('hr.department', string='Department', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', tracking=True)
    activity = fields.Char(string='Activity Description', required=True, tracking=True)
    
    # Generic Reference for Future Integrations (e.g., Purchase Order, Fleet Log)
    source_model = fields.Char(string='Source Model', help="Model name of the source document (e.g., 'purchase.order').")
    source_record_id = fields.Many2oneReference(string='Source Record ID', model_field='source_model', help="ID of the source document.")
    
    emission_factor_id = fields.Many2one('eco.emission.factor', string='Emission Factor', required=True, tracking=True)
    quantity = fields.Float(string='Quantity', required=True, tracking=True)
    
    calculated_emission = fields.Float(
        string='Calculated Emission (CO2e)',
        compute='_compute_calculated_emission',
        store=True,
        tracking=True
    )
    
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True, tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    @api.depends('quantity', 'emission_factor_id.factor')
    def _compute_calculated_emission(self):
        for record in self:
            if record.emission_factor_id:
                record.calculated_emission = record.quantity * record.emission_factor_id.factor
            else:
                record.calculated_emission = 0.0

    def action_confirm(self):
        """
        Confirms the transaction, triggers score recalculation, and checks thresholds.
        """
        departments = self.env['hr.department']
        for record in self:
            record.status = 'confirmed'
            departments |= record.department_id
            record._check_emission_threshold()
            
        # Update metrics once per affected department (Rule 3 & 4)
        for dept in departments:
            self.env['eco.score.engine'].update_department_metrics(dept)
        return True
            
    def action_cancel(self):
        for record in self:
            record.status = 'cancelled'
        return True

    def action_draft(self):
        for record in self:
            record.status = 'draft'
        return True

    def _check_emission_threshold(self):
        """
        Rule 5: If emissions exceed configurable threshold, prepare notification hook.
        """
        self.ensure_one()
        # Placeholder for configuration setting threshold
        threshold = 1000.0 
        if self.calculated_emission > threshold:
            # TODO: Implementation point for future module (e.g. eco_social or eco_reports)
            pass
