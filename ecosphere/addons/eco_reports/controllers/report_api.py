from odoo import http
from odoo.http import request

class ReportAPI(http.Controller):

    @http.route('/reports/api/definitions', type='json', auth='user')
    def get_definitions(self, **kwargs):
        defs = request.env['eco.report.definition'].search_read([('active', '=', True)], ['id', 'name', 'export_formats'])
        return {'reports': defs}

    @http.route('/reports/api/generate', type='json', auth='user')
    def generate_report(self, report_definition_id, filters, export_format, **kwargs):
        return request.env['eco.report.builder'].generate(
            report_definition_id,
            filters=filters,
            export_format=export_format
        )
