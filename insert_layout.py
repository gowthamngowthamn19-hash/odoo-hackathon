import sys
sys.path.append(r'C:\Program Files\Odoo 18.0.20260921\server')
import odoo
from odoo import api, SUPERUSER_ID

odoo.tools.config.parse_config(['-c', r'c:\Users\Admin\odoo-hackathon\odoo.conf', '-d', 'ecosphere'])
registry = odoo.registry('ecosphere')

with registry.cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})
    Layout = env['eco.dashboard.layout']

    existing = Layout.search_count([])
    print("Existing layout records:", existing)

    if existing == 0:
        layouts = [
            {'name': 'Overall ESG Score', 'widget_name': 'overall_esg', 'width': 1, 'height': 1, 'sequence': 10, 'dashboard_type': 'executive'},
            {'name': 'Environmental Score', 'widget_name': 'env_score', 'width': 1, 'height': 1, 'sequence': 20, 'dashboard_type': 'executive'},
            {'name': 'Social Score', 'widget_name': 'social_score', 'width': 1, 'height': 1, 'sequence': 30, 'dashboard_type': 'executive'},
            {'name': 'Governance Score', 'widget_name': 'gov_score', 'width': 1, 'height': 1, 'sequence': 40, 'dashboard_type': 'executive'},
            {'name': 'Carbon Trend', 'widget_name': 'carbon_trend', 'width': 2, 'height': 2, 'sequence': 50, 'dashboard_type': 'executive'},
            {'name': 'ESG Distribution', 'widget_name': 'esg_distribution', 'width': 1, 'height': 2, 'sequence': 60, 'dashboard_type': 'executive'},
            {'name': 'Department Comparison', 'widget_name': 'dept_comparison', 'width': 1, 'height': 2, 'sequence': 70, 'dashboard_type': 'executive'},
            {'name': 'Leaderboard', 'widget_name': 'leaderboard', 'width': 2, 'height': 1, 'sequence': 80, 'dashboard_type': 'executive'},
            {'name': 'Recent Activity', 'widget_name': 'recent_activity', 'width': 1, 'height': 1, 'sequence': 90, 'dashboard_type': 'executive'},
            {'name': 'Goal Tracker', 'widget_name': 'goal_tracker', 'width': 1, 'height': 1, 'sequence': 100, 'dashboard_type': 'executive'},
            {'name': 'AI Insights', 'widget_name': 'ai_insights', 'width': 2, 'height': 1, 'sequence': 110, 'dashboard_type': 'executive'},
            {'name': 'Notifications', 'widget_name': 'notifications', 'width': 2, 'height': 1, 'sequence': 120, 'dashboard_type': 'executive'},
        ]
        for l in layouts:
            Layout.create(l)
            print("Created layout:", l['widget_name'])
        cr.commit()
        print("All layout records created successfully.")
    else:
        print("Layout records already exist, skipping.")
