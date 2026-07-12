from odoo import models, api

class AnalyticsService(models.AbstractModel):
    _name = 'eco.analytics.service'
    _description = 'Chart Data Aggregation Service'

    @api.model
    def get_chart_data(self, chart_type):
        if chart_type == 'carbon_trend':
            return self._get_carbon_trend()
        if chart_type == 'dept_comparison':
            return self._get_dept_comparison()
        if chart_type == 'esg_distribution':
            return self._get_esg_distribution()
        return {}

    def _get_carbon_trend(self):
        self.env.cr.execute("""
            SELECT to_char(date, 'Mon YYYY') as month, SUM(calculated_emission) as total
            FROM eco_carbon_transaction
            WHERE status = 'confirmed'
            GROUP BY to_char(date, 'Mon YYYY'), date_trunc('month', date)
            ORDER BY date_trunc('month', date) ASC
            LIMIT 12
        """)
        res = self.env.cr.dictfetchall()
        
        # Mock data if no transactions exist for the hackathon demo
        if not res:
            res = [{'month': 'Jan 2026', 'total': 1200}, {'month': 'Feb 2026', 'total': 1100}, {'month': 'Mar 2026', 'total': 900}]

        return {
            'labels': [r['month'] for r in res],
            'datasets': [{
                'label': 'Carbon Emissions (kg)',
                'data': [r['total'] for r in res],
                'borderColor': '#10b981',
                'backgroundColor': 'rgba(16, 185, 129, 0.2)',
                'tension': 0.4,
                'fill': True
            }]
        }

    def _get_dept_comparison(self):
        self.env.cr.execute("""
            SELECT name, environment_score, social_score, governance_score 
            FROM hr_department 
            WHERE active = True
        """)
        res = self.env.cr.dictfetchall()
        
        if not res:
            res = [{'name': 'Sales', 'environment_score': 70, 'social_score': 80, 'governance_score': 90}]

        labels = [r['name'] for r in res]
        return {
            'labels': labels,
            'datasets': [
                {'label': 'Environment', 'data': [r['environment_score'] or 0 for r in res], 'backgroundColor': '#10b981'},
                {'label': 'Social', 'data': [r['social_score'] or 0 for r in res], 'backgroundColor': '#3b82f6'},
                {'label': 'Governance', 'data': [r['governance_score'] or 0 for r in res], 'backgroundColor': '#8b5cf6'}
            ]
        }

    def _get_esg_distribution(self):
        kpis = self.env['eco.kpi.service'].get_kpis()
        return {
            'labels': ['Environment', 'Social', 'Governance'],
            'datasets': [{
                'data': [kpis['env_score']['value'], kpis['social_score']['value'], kpis['gov_score']['value']],
                'backgroundColor': ['#10b981', '#3b82f6', '#8b5cf6'],
                'hoverOffset': 4
            }]
        }
