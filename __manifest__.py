# -*- coding: utf-8 -*-
{
    'name': "phones",

    'summary': """
    """,

    'description': """
    """,

    'author': "Alexander",
    'website': "https://www.linkedin.com/in/alexander-tarletsky/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extension',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
