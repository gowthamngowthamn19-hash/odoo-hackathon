from odoo import http
from odoo.http import request

class AI_API(http.Controller):

    @http.route('/ai/report', type='json', auth='user')
    def generate_report(self, filters=None, **kwargs):
        summary = request.env['eco.ai.gateway'].generate_executive_summary(filters)
        return {'status': 'success', 'summary': summary}

    @http.route('/ai/recommend', type='json', auth='user')
    def recommend(self, department_id, **kwargs):
        recommendations = request.env['eco.ai.gateway'].get_recommendations(department_id)
        return {'status': 'success', 'recommendations': recommendations}

    @http.route('/ai/forecast', type='json', auth='user')
    def forecast(self, filters=None, **kwargs):
        forecast = request.env['eco.ai.prediction.engine'].forecast_carbon(filters)
        return {'status': 'success', 'forecast': forecast}
        
    @http.route('/ai/history', type='json', auth='user')
    def history(self, **kwargs):
        usage = request.env['eco.ai.usage'].search_read([('user_id', '=', request.env.user.id)], limit=50)
        return {'history': usage}
