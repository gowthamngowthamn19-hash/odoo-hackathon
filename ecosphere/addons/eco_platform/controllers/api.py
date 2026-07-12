from odoo import http
from odoo.http import request

class CoreAPIController(http.Controller):

    @http.route('/api/registry', type='json', auth='user')
    def get_registry(self):
        endpoints = request.env['eco.api.registry'].search_read([('status', '=', 'active')])
        return {'endpoints': endpoints}
