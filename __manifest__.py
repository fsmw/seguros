# -*- coding: utf-8 -*-
{
    'name': "seguros",

    'summary': """
        Ejemplo de desarrollo en Odoo, este cambio lo hizo el compañero 2""",

    'description': """
        Sistema que permite administras las polizas de seguro
        de los clientes de la compañia
    """,

    'author': "UTAL",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_poliza.xml',
        # 'views/templates.xml',
    ],
}
