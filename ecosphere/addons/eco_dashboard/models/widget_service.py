from odoo import models, api

class WidgetService(models.AbstractModel):
    _name = 'eco.widget.service'
    _description = 'Dashboard Widget Registry'

    @api.model
    def get_available_widgets(self):
        """ 
        Returns a dictionary of all registered backend widgets.
        Other modules can override this to inject new widgets.
        """
        return {
            'overall_esg': {'type': 'kpi', 'title': 'Overall ESG Score', 'icon': 'fa-globe'},
            'env_score': {'type': 'kpi', 'title': 'Environmental Score', 'icon': 'fa-leaf'},
            'social_score': {'type': 'kpi', 'title': 'Social Score', 'icon': 'fa-users'},
            'gov_score': {'type': 'kpi', 'title': 'Governance Score', 'icon': 'fa-balance-scale'},
            'carbon_trend': {'type': 'chart', 'title': 'Carbon Trend', 'chart_type': 'line'},
            'dept_comparison': {'type': 'chart', 'title': 'Department Comparison', 'chart_type': 'bar'},
            'esg_distribution': {'type': 'chart', 'title': 'ESG Distribution', 'chart_type': 'doughnut'},
            'compliance_trend': {'type': 'chart', 'title': 'Compliance Trend', 'chart_type': 'bar'},
            'leaderboard': {'type': 'leaderboard', 'title': 'Top Employees'},
            'recent_activity': {'type': 'activity', 'title': 'Recent Activities'},
            'goal_tracker': {'type': 'goal', 'title': 'Goal Progress'},
            'notifications': {'type': 'notification', 'title': 'Alerts & Reminders'},
            'ai_insights': {'type': 'ai', 'title': 'EcoSphere AI Insights'}
        }
