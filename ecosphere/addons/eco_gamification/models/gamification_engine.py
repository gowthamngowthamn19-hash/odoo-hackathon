from odoo import models, api

class GamificationEngine(models.AbstractModel):
    _name = 'eco.gamification.engine'
    _description = 'Gamification Facade'

    @api.model
    def emit_event(self, event_code, employee, reference_model, reference_id, event_name="", metadata=None):
        """ 
        Emits a gamification event.
        This is the single entry point for all other ESG modules.
        """
        event = self.env['eco.gamification.event'].create({
            'event_code': event_code,
            'event_name': event_name or event_code,
            'employee_id': employee.id,
            'reference_model': reference_model,
            'reference_id': reference_id,
            'metadata': metadata or {}
        })
        
        # Trigger processor synchronously
        self.env['eco.event.processor'].process_pending_events()

    @api.model
    def get_employee_xp(self, employee):
        """ Returns the exact XP balance computed from the transaction ledger. """
        self.env.cr.execute("""
            SELECT SUM(xp) FROM eco_xp_transaction WHERE employee_id = %s
        """, (employee.id,))
        result = self.env.cr.fetchone()
        return result[0] or 0

    @api.model
    def _prepare_notification(self, event_code, event_record):
        """ Hook for future Notification and AI Modules. """
        pass
