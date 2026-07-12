from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    carbon_footprint = fields.Float(
        string='Carbon Footprint (CO2e)', 
        help="Estimated carbon footprint per unit of this product."
    )
    recyclable = fields.Boolean(string='Is Recyclable', default=False)
    green_score = fields.Float(
        string='Green Score', 
        help="Internal sustainability score for this product (0-100)."
    )
    supplier_rating = fields.Selection([
        ('a', 'A - Excellent'),
        ('b', 'B - Good'),
        ('c', 'C - Average'),
        ('d', 'D - Poor'),
        ('f', 'F - Unacceptable')
    ], string='Supplier ESG Rating')
    packaging_notes = fields.Text(
        string='Packaging Notes', 
        help="Details about sustainable packaging used for this product."
    )
