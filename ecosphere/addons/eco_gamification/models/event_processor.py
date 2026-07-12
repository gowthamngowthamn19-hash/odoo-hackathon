from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class EventProcessor(models.AbstractModel):
    _name = 'eco.event.processor'
    _description = 'Event Processor Service'

    @api.model
    def process_pending_events(self):
        """ Fetch all pending events and process them synchronously. """
        events = self.env['eco.gamification.event'].search([('status', '=', 'pending')], order='created_date asc')
        
        for event in events:
            try:
                self._process_event(event)
            except Exception as e:
                _logger.error("Failed to process event %s: %s", event.id, str(e))
                event.write({'status': 'failed', 'processed_date': fields.Datetime.now()})

    def _process_event(self, event):
        """ Core logic mapping events to the Gamification workflow. """
        # 1. Map to XP Rule and create XP Transaction
        self.env['eco.xp.service'].process_xp_for_event(event)
        
        # 2. Trigger Badge Checks
        self.env['eco.badge.engine'].check_and_award_badges(event.employee_id)
        
        # 3. Trigger Leaderboard Update / Hook
        self.env['eco.leaderboard.service'].trigger_update()
        
        # 4. Trigger Future Notification / AI Hooks
        self.env['eco.gamification.engine']._prepare_notification(event.event_code, event)
        
        # Mark as processed
        event.write({
            'status': 'processed',
            'processed_date': fields.Datetime.now()
        })
