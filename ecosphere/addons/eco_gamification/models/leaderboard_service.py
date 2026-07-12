from odoo import models, api

class LeaderboardService(models.AbstractModel):
    _name = 'eco.leaderboard.service'
    _description = 'Leaderboard Service Hook'

    @api.model
    def trigger_update(self):
        """ 
        Hook called by the event processor. 
        Currently leaderboard is a dynamic SQL view, so no manual refresh is needed.
        """
        pass
