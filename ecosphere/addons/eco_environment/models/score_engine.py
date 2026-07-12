from odoo import models, api

class ScoreEngine(models.AbstractModel):
    _name = 'eco.score.engine'
    _description = 'Environmental Score Engine'

    @api.model
    def update_department_metrics(self, department):
        """
        Recalculates the environmental score and goal progress for the given department.
        Centralizes the business logic separate from the data models.
        """
        # 1. Fetch relevant confirmed transactions for the department
        transactions = self.env['eco.carbon.transaction'].search([
            ('department_id', '=', department.id),
            ('status', '=', 'confirmed')
        ])
        
        total_emissions = sum(transactions.mapped('calculated_emission'))
        
        # 2. Calculate and update Score
        # Simple scoring logic: base 100, drops proportionally to emissions.
        # (Assuming 10,000 CO2e completely depletes the environmental score)
        score = max(0.0, 100.0 - (total_emissions / 100.0))
        department.environment_score = score
        
        # 3. Update Goals Progress (Workflow Rule 4)
        goals = self.env['eco.environmental.goal'].search([
            ('department_id', '=', department.id),
            ('status', 'in', ['draft', 'active'])
        ])
        
        for goal in goals:
            # We map the total emissions as the current value of their environmental goals.
            goal.current_value = total_emissions
