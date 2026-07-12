from odoo import http
from odoo.http import request

class WebhookController(http.Controller):

    @http.route('/webhook/generic', type='json', auth='none', methods=['POST'])
    def handle_webhook(self, **kwargs):
        # Publish external webhook to the internal event bus
        payload = request.jsonrequest
        request.env['eco.event.bus'].sudo().publish('webhook.received', payload)
        return {'status': 'received'}
