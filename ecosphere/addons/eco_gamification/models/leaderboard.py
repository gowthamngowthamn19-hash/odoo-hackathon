from odoo import models, fields, tools

class EcoLeaderboard(models.Model):
    _name = 'eco.leaderboard'
    _description = 'Gamification Leaderboard'
    _auto = False
    
    employee_id = fields.Many2one('hr.employee', string='Employee', readonly=True)
    department_id = fields.Many2one('hr.department', string='Department', readonly=True)
    total_xp = fields.Integer(string='Total XP', readonly=True)
    completed_challenges = fields.Integer(string='Completed Challenges', readonly=True)
    badge_count = fields.Integer(string='Badges', readonly=True)
    rank = fields.Integer(string='Rank', readonly=True)
    
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW %s AS (
                SELECT 
                    e.id as id,
                    e.id as employee_id,
                    e.department_id,
                    COALESCE((SELECT SUM(xp) FROM eco_xp_transaction WHERE employee_id = e.id), 0) as total_xp,
                    COALESCE((SELECT COUNT(id) FROM eco_employee_participation WHERE employee_id = e.id AND status = 'completed'), 0) as completed_challenges,
                    COALESCE((SELECT COUNT(id) FROM eco_employee_badge WHERE employee_id = e.id), 0) as badge_count,
                    RANK() OVER (ORDER BY COALESCE((SELECT SUM(xp) FROM eco_xp_transaction WHERE employee_id = e.id), 0) DESC, COALESCE((SELECT COUNT(id) FROM eco_employee_participation WHERE employee_id = e.id AND status = 'completed'), 0) DESC) as rank
                FROM hr_employee e
            )
        ''' % self._table)
