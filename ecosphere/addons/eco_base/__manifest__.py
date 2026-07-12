{
    'name': 'EcoSphere Base',
    'version': '1.0',
    'summary': 'Foundational module for EcoSphere ESG Management Platform',
    'description': 'Core models and settings for the EcoSphere ESG application.',
    'category': 'Sustainability/ESG',
    'author': 'EcoSphere Team',
    'depends': ['base', 'mail', 'hr', 'web'],
    'data': [
        'security/eco_security.xml',
        'security/ir.model.access.csv',
        'data/default_data.xml',
        'views/menu_roots.xml',
        'views/dashboard_views.xml',
        'views/category_views.xml',
        'views/badge_views.xml',
        'views/reward_views.xml',
        'views/settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'eco_base/static/src/js/dashboard.js',
            'eco_base/static/src/xml/dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
