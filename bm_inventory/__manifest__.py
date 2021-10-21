# -*- coding: utf-8 -*-
{
    'name': "bista_odoo14",
    'summary': """this is  bista new project""",
    'description': """this project was related to inventory""",
    'author': "Bista Solutions pvbt.ltd",
    'website': "http://www.bistasolutions.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'report/stock_picking_report.xml',
        'report/inventory_delivery_slip_report.xml',
        'report/report_location_barcode.xml',
        'report/product_label_report.xml',
    ],
    'installable': True,
    'auto_install': True,
}
