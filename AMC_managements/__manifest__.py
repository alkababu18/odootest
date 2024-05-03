# -*- coding: utf-8 -*-
{
    'name': 'AMC_managements',
    'author': 'Alka',
    'version': '1.0',
    'summary': 'Module to manage contracts',
    'sequence': 10,
    'description': """AMC Management Module""",
    'category': 'Contract',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/email_template.xml',
        'views/contract_management_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}