# -*- coding: utf-8 -*-
{
    'name': "academia",

    'summary': """
        nueva academia""",

    'description': """
      modulo de entrenamiento Desarrollo junior 2020
    """,

    'author': "Todoo SAS",
    'website': "http://www.Todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academia',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/vista_academia.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
      #  'demo/demo.xml',
    ],
    
    
}
