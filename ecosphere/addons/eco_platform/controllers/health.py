from odoo import http
from odoo.http import request

class HealthController(http.Controller):

    @http.route('/health', type='json', auth='none')
    def health_check(self):
        # Extremely basic health check
        return {
            'status': 'ok',
            'database': 'connected',
            'version': '18.0.1.0.0'
        }
