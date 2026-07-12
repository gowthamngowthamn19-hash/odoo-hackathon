from odoo import models, fields, api

class DashboardLayout(models.Model):
    _name = 'eco.dashboard.layout'
    _description = 'Dashboard Layout Configuration'
    _order = 'dashboard_type, user_id, sequence'

    name = fields.Char(string='Layout Name', required=True)
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade', index=True)
    widget_name = fields.Char(string='Widget ID', required=True, help="Must match a registered OWL widget name")
    
    position_x = fields.Integer(string='Position X', default=0)
    position_y = fields.Integer(string='Position Y', default=0)
    width = fields.Integer(string='Width', default=1, required=True)
    height = fields.Integer(string='Height', default=1, required=True)
    
    visible = fields.Boolean(string='Visible', default=True)
    sequence = fields.Integer(string='Sequence', default=10)
    
    dashboard_type = fields.Selection([
        ('executive', 'Executive'),
        ('department', 'Department'),
        ('personal', 'Personal')
    ], string='Dashboard Type', default='executive', required=True)
    
    @api.model
    def load_user_layout(self, dashboard_type='executive'):
        """ Returns the layout for the current user, or falls back to admin default. """
        domain = [('dashboard_type', '=', dashboard_type), ('user_id', '=', self.env.uid), ('visible', '=', True)]
        layouts = self.search(domain)
        
        if not layouts:
            # Fallback to default (user_id = False)
            domain = [('dashboard_type', '=', dashboard_type), ('user_id', '=', False), ('visible', '=', True)]
            layouts = self.search(domain)
            
        return layouts.read(['widget_name', 'position_x', 'position_y', 'width', 'height', 'sequence'])
