from odoo import models

class EcoDashboard(models.AbstractModel):
    """
    Abstract model for the dashboard.
    Will be used later if we need to return server-side dashboard statistics
    to an OWL component.
    """
    _name = 'eco.dashboard'
    _description = 'ESG Dashboard Stats'
