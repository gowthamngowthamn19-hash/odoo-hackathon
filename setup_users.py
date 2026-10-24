import sys
sys.path.append(r'C:\Program Files\Odoo 18.0.20260921\server')
import odoo
from odoo import api, SUPERUSER_ID

odoo.tools.config.parse_config(['-c', r'c:\Users\Admin\odoo-hackathon\odoo.conf', '-d', 'ecosphere'])
registry = odoo.registry('ecosphere')

with registry.cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # 1. Ensure admin has password 'admin'
    admin = env.ref('base.user_admin')
    admin.password = 'admin'
    
    # 2. Setup demo users from README
    users_to_create = [
        {
            'name': 'ESG Manager',
            'login': 'esg@eco.com',
            'password': 'admin',
            'group_xml_id': 'eco_base.group_eco_manager',
        },
        {
            'name': 'HR Department Head',
            'login': 'hr@eco.com',
            'password': 'admin',
            'group_xml_id': 'eco_base.group_eco_department_head',
        },
        {
            'name': 'Pooja Employee',
            'login': 'pooja@eco.com',
            'password': 'admin',
            'group_xml_id': 'eco_base.group_eco_employee',
        },
    ]
    
    for u in users_to_create:
        existing = env['res.users'].search([('login', '=', u['login'])], limit=1)
        group = env.ref(u['group_xml_id'], raise_if_not_found=False)
        group_user = env.ref('base.group_user')
        groups = [(4, group_user.id)]
        if group:
            groups.append((4, group.id))
            
        if not existing:
            env['res.users'].create({
                'name': u['name'],
                'login': u['login'],
                'password': u['password'],
                'groups_id': groups,
            })
            print(f"Created user {u['login']}")
        else:
            existing.password = u['password']
            if group:
                existing.write({'groups_id': [(4, group.id)]})
            print(f"Updated user {u['login']}")
            
    cr.commit()
    print("All demo users configured successfully.")
