from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_emission_calculation = fields.Boolean(string='Auto Emission Calculation', config_parameter='eco_base.auto_emission_calculation')
    auto_badge_award = fields.Boolean(string='Auto Badge Award', config_parameter='eco_base.auto_badge_award')
    require_csr_evidence = fields.Boolean(string='Require CSR Evidence', config_parameter='eco_base.require_csr_evidence')
    
    environment_weight = fields.Float(string='Environment Weight (%)', default=33.33, config_parameter='eco_base.environment_weight')
    social_weight = fields.Float(string='Social Weight (%)', default=33.33, config_parameter='eco_base.social_weight')
    governance_weight = fields.Float(string='Governance Weight (%)', default=33.34, config_parameter='eco_base.governance_weight')
    
    notification_enabled = fields.Boolean(string='Enable ESG Notifications', config_parameter='eco_base.notification_enabled')
