{
    'name': 'Product Completeness Tracker',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Products',
    'summary': 'Progress bar on product list showing data completeness — highlights missing image, description, price, and category.',
    'description': """
Product Completeness Tracker for Odoo 19 (Free / LGPL-3)
=========================================================
- Color-coded progress bar (green/yellow/red) directly in the product list
- "Incomplete Products" filter to instantly find products missing key data
- "Missing Fields" column listing exactly which fields need attention
- Tracks: Product Name, Sales Description, Sale Price, Image, Category
- Zero configuration — install and go
    """,
    'author': 'Randy Nguyen',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['product', 'web'],
    'data': [
        'views/product-completeness-views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'product_completeness_tracker/static/src/css/product-completeness.css',
            'product_completeness_tracker/static/src/xml/product-completeness-widget.xml',
            'product_completeness_tracker/static/src/js/product-completeness-widget.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
