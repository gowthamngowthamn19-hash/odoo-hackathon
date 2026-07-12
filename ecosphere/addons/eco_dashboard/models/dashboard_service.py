from odoo import models, api

class DashboardService(models.AbstractModel):
    _name = 'eco.dashboard.service'
    _description = 'Main Dashboard Orchestrator'

    @api.model
    def get_dashboard_data(self):
        """ Returns all required data for the initial dashboard load. """
        layout = self.env['eco.dashboard.layout'].load_user_layout()
        kpis = self.env['eco.kpi.service'].get_kpis()
        available_widgets = self.env['eco.widget.service'].get_available_widgets()
        
        return {
            'layout': layout,
            'kpis': kpis,
            'available_widgets': available_widgets,
        }
