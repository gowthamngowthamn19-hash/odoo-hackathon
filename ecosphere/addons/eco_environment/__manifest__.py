{
    'name': 'EcoSphere - Environment',
    'version': '18.0.1.0.0',
    'category': 'Sustainability',
    'summary': 'Environmental Management for EcoSphere',
    'description': """
        Environmental Management Module
        - Carbon Accounting
        - Emission Factors
        - Environmental Goals
        - Product ESG Profiles
        - Department Environmental Score
    """,
    'depends': ['eco_base', 'mail', 'hr', 'product', 'eco_platform'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_roots.xml',
        'views/emission_factor_views.xml',
        'views/carbon_transaction_views.xml',
        'views/environmental_goal_views.xml',
        'views/product_esg_views.xml',
        'data/demo_data.xml',
        'views/menu_actions.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
