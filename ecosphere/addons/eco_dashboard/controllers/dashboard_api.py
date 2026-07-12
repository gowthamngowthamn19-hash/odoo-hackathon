from odoo import http
from odoo.http import request

class DashboardAPI(http.Controller):

    @http.route('/dashboard/api/init', type='json', auth='user')
    def init_dashboard(self, **kwargs):
        return request.env['eco.dashboard.service'].get_dashboard_data()

    @http.route('/dashboard/api/kpis', type='json', auth='user')
    def get_kpis(self, **kwargs):
        return request.env['eco.kpi.service'].get_kpis()

    @http.route('/dashboard/api/charts', type='json', auth='user')
    def get_charts(self, chart_type, **kwargs):
        return request.env['eco.analytics.service'].get_chart_data(chart_type)

    @http.route('/dashboard/api/layout/save', type='json', auth='user')
    def save_layout(self, layout_data, **kwargs):
        # Stub for saving resized/moved layout config
        return {'status': 'success'}
