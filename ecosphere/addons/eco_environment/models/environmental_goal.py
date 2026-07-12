from odoo import models, fields, api, _

class EnvironmentalGoal(models.Model):
    _name = 'eco.environmental.goal'
    _description = 'Environmental Goal'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Goal Name', required=True, tracking=True)
    department_id = fields.Many2one('hr.department', string='Department', required=True, tracking=True)
    
    current_value = fields.Float(string='Current Value', default=0.0, tracking=True, help="Automatically updated via Score Engine")
    target_value = fields.Float(string='Target Value', required=True, tracking=True)
    deadline = fields.Date(string='Deadline', required=True, tracking=True)
    
    progress = fields.Float(string='Progress (%)', compute='_compute_progress', store=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('expired', 'Expired')
    ], string='Status', compute='_compute_status', store=True, tracking=True, default='draft')

    @api.depends('current_value', 'target_value')
    def _compute_progress(self):
        for goal in self:
            if goal.target_value:
                # Calculate simple percentage towards target
                progress = (goal.current_value / goal.target_value) * 100.0
                goal.progress = min(max(progress, 0.0), 100.0)
            else:
                goal.progress = 0.0

    @api.depends('current_value', 'target_value', 'deadline')
    def _compute_status(self):
        today = fields.Date.context_today(self)
        for goal in self:
            # Preserve draft state for setup
            if goal.status == 'draft' and goal.current_value == 0:
                continue
                
            if goal.target_value > 0 and goal.current_value >= goal.target_value:
                goal.status = 'completed'
            elif goal.deadline and goal.deadline < today:
                goal.status = 'expired'
            else:
                goal.status = 'active'

    def action_activate(self):
        for record in self:
            record.status = 'active'
            record._compute_status()
