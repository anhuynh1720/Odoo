{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "An",
    'category': 'Sales',
    'description': """
    Description text
    """,
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'application': True,
}