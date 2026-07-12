from odoo import models, api

class SocialScoreEngine(models.AbstractModel):
    _name = 'eco.social.score.engine'
    _description = 'Social Score Engine'

    @api.model
    def update_department_social_metrics(self, departments):
        """
        Recalculates the social score for the given departments.
        Optimized to handle recordsets natively.
        """
        for department in departments:
            score = 0.0
            
            # 1. Volunteer Hours Factor (e.g. 1 point per 10 hours, up to 40)
            participations = self.env['eco.employee.participation'].search([
                ('department_id', '=', department.id),
                ('status', '=', 'approved')
            ])
            total_hours = sum(participations.mapped('hours_credited'))
            score += min(40.0, total_hours / 10.0)

            # 2. Training Completions Factor (e.g. 5 points per verified training, up to 30)
            completions_count = self.env['eco.social.training.completion'].search_count([
                ('department_id', '=', department.id),
                ('status', '=', 'verified')
            ])
            score += min(30.0, completions_count * 5.0)

            # 3. Diversity Factor (e.g. up to 30 points based on latest confirmed metric)
            latest_metric = self.env['eco.diversity.metric'].search([
                ('department_id', '=', department.id),
                ('status', '=', 'confirmed')
            ], order='date desc', limit=1)
            
            if latest_metric:
                female_score = min(15.0, (latest_metric.female_ratio / 50.0) * 15.0)
                minority_score = min(15.0, (latest_metric.minority_ratio / 30.0) * 15.0)
                score += female_score + minority_score

            # Ensure score stays within 0-100 range and update the department record
            department.social_score = min(100.0, max(0.0, score))
