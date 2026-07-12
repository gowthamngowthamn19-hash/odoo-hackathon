from odoo import models, fields, api

class GenerateReportWizard(models.TransientModel):
    _name = 'eco.report.generate.wizard'
    _description = 'Generate Report Wizard'
    
    report_definition_id = fields.Many2one('eco.report.definition', string='Report Type', required=True, domain="[('active', '=', True)]")
    export_format = fields.Selection(related='report_definition_id.export_formats', readonly=False)
    
    # Common Filters
    department_id = fields.Many2one('hr.department', string='Department')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    
    def action_generate(self):
        filters = {
            'department_id': self.department_id.id,
            'employee_id': self.employee_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to
        }
        
        return self.env['eco.report.builder'].generate(
            self.report_definition_id.id,
            filters=filters,
            export_format=self.export_format
        )
