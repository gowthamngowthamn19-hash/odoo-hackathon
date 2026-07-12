from odoo import models, api

class KPIService(models.AbstractModel):
    _name = 'eco.kpi.service'
    _description = 'Dashboard KPI Aggregation Service'

    @api.model
    def get_kpis(self):
        """ 
        Aggregates KPIs without business logic calculations. 
        Uses read_group and simple sum/avg queries.
        """
        self.env.cr.execute("""
            SELECT 
                AVG(environment_score) as env_score,
                AVG(social_score) as soc_score,
                AVG(governance_score) as gov_score
            FROM hr_department
        """)
        scores = self.env.cr.dictfetchone() or {}
        
        env = scores.get('env_score') or 0
        soc = scores.get('soc_score') or 0
        gov = scores.get('gov_score') or 0
        overall = (env + soc + gov) / 3 if (env + soc + gov) > 0 else 0

        self.env.cr.execute("""
            SELECT SUM(calculated_emission) 
            FROM eco_carbon_transaction 
            WHERE status = 'confirmed' AND DATE(date) = CURRENT_DATE
        """)
        carbon_today = self.env.cr.fetchone()
        carbon_today = carbon_today[0] if carbon_today and carbon_today[0] is not None else 0
        
        current_xp = 0
        user_emp = self.env.user.employee_id
        if user_emp:
            current_xp = self.env['eco.gamification.engine'].get_employee_xp(user_emp)
            
        return {
            'overall_esg': {'value': round(overall, 1), 'suffix': '/100', 'color': 'text-primary'},
            'env_score': {'value': round(env, 1), 'suffix': '/100', 'color': 'text-success'},
            'social_score': {'value': round(soc, 1), 'suffix': '/100', 'color': 'text-info'},
            'gov_score': {'value': round(gov, 1), 'suffix': '/100', 'color': 'text-warning'},
            'carbon_today': {'value': round(carbon_today, 2), 'suffix': ' kg', 'color': 'text-danger'},
            'current_xp': {'value': current_xp, 'suffix': ' XP', 'color': 'text-warning'}
        }
