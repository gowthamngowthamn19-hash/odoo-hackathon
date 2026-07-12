{
    'name': 'EcoSphere - Governance',
    'version': '18.0.1.0.0',
    'category': 'Sustainability',
    'summary': 'Governance Management for EcoSphere',
    'description': """
        Governance Management Module
        - ESG Policies
        - Policy Acknowledgements
        - ESG Audits
        - Compliance Issues
        - Governance Score Engine
    """,
    'depends': ['eco_base', 'mail', 'hr', 'eco_platform'],
    'data': [
        'security/ir.model.access.csv',
        'views/esg_policy_views.xml',
        'views/policy_acknowledgement_views.xml',
        'views/esg_audit_views.xml',
        'views/compliance_issue_views.xml',
        'data/demo_data.xml',
        'views/menu_actions.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
