{
    'name': 'EcoSphere - Social',
    'version': '18.0.1.0.0',
    'category': 'Sustainability',
    'summary': 'Social Management for EcoSphere',
    'summary': 'Corporate Social Responsibility Module',
    'description': """
        Social Management Module
        - CSR Activities
        - Employee Volunteering
        - Diversity Metrics
        - ESG Training
        - Social Score Engine
    """,
    'depends': ['eco_base', 'eco_environment', 'eco_platform'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_roots.xml',
        'views/csr_activity_views.xml',
        'views/employee_participation_views.xml',
        'views/diversity_metric_views.xml',
        'views/training_views.xml',
        'views/hr_employee_views.xml',
        'data/demo_data.xml',
        'views/menu_actions.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
