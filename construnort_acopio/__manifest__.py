{
    'name': 'Construnort Acopio',
    'version': '15.0.1.0.0',
    'summary': 'Agrega estado acopio y wizard a sale.order',
    'category': 'Sales',
    'author': 'Tu Empresa',
    'website': '',
    'license': 'AGPL-3',
    'depends': ['sale'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/sale_order_acopio_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
