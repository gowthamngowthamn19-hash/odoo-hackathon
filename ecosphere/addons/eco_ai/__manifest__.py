{
    'name': 'EcoSphere AI',
    'version': '18.0.1.0.0',
    'category': 'Environment',
    'summary': 'Enterprise AI Engine powered by Groq',
    'depends': ['eco_base', 'eco_environment', 'eco_social', 'eco_governance', 'eco_gamification', 'eco_dashboard', 'eco_reports', 'eco_platform', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/default_prompts.xml',
        'views/menu_roots.xml',
        'views/ai_settings.xml',
        'views/ai_history.xml',
        'views/menu_actions.xml',
    ],
    'installable': True,
    'application': True,
    'external_dependencies': {
        'python': ['groq'],
    },
}
