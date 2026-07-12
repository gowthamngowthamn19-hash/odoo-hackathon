from odoo import models, api

class XPService(models.AbstractModel):
    _name = 'eco.xp.service'
    _description = 'XP Processing Service'

    @api.model
    def process_xp_for_event(self, event):
        """ Converts an event into an XP transaction if an active rule matches. """
        # Prevent duplicates for the same event
        existing_tx = self.env['eco.xp.transaction'].search([
            ('reference_model', '=', event.reference_model),
            ('reference_id', '=', event.reference_id),
            ('reason', '=', event.event_code)
        ], limit=1)
        
        if existing_tx:
            return

        rule = self.env['eco.xp.rule'].search([
            ('action_code', '=', event.event_code), 
            ('enabled', '=', True)
        ], limit=1)
        
        xp_amount = 0
        if rule:
            xp_amount = rule.xp_value
        elif event.metadata and event.metadata.get('fallback_xp'):
            xp_amount = event.metadata.get('fallback_xp')
            
        if xp_amount != 0:
            transaction_type = 'earn' if xp_amount > 0 else 'redeem'
            
            self.env['eco.xp.transaction'].create({
                'employee_id': event.employee_id.id,
                'reference_model': event.reference_model,
                'reference_id': event.reference_id,
                'reason': event.event_code,
                'xp': xp_amount,
                'transaction_type': transaction_type
            })
