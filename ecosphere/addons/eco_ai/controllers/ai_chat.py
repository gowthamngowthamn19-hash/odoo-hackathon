from odoo import http
from odoo.http import request

class AIChatController(http.Controller):

    @http.route('/ai/chat', type='json', auth='user')
    def chat(self, question, conversation_id=None, filters=None, **kwargs):
        gateway = request.env['eco.ai.gateway']
        
        # Synchronous return of Chat response
        response = gateway.ask_copilot(question, filters)
        
        return {
            'status': 'success',
            'response': response
        }
