from odoo import api, fields, models

# (field_name, display_label) — each worth 1 point out of TOTAL_FIELDS
_TRACKED = [
    ('name', 'Product Name'),
    ('description_sale', 'Sales Description'),
    ('categ_id', 'Category'),
    ('image_1920', 'Product Image'),
    ('list_price', 'Sale Price'),
]
_TOTAL = len(_TRACKED)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pct_completeness = fields.Float(
        string='Completeness (%)',
        compute='_compute_pct_completeness',
        store=True,
        digits=(5, 1),
        help='Percentage of key product fields that are filled in.',
    )
    pct_missing_fields = fields.Char(
        string='Missing Fields',
        compute='_compute_pct_completeness',
        store=True,
        help='Comma-separated list of fields that still need to be filled in.',
    )

    @api.depends('name', 'description_sale', 'categ_id', 'image_1920', 'list_price')
    def _compute_pct_completeness(self):
        for product in self:
            missing = []
            score = 0
            for fname, label in _TRACKED:
                val = product[fname]
                # list_price is "complete" only when explicitly > 0
                if fname == 'list_price':
                    filled = bool(val and val > 0)
                else:
                    filled = bool(val)
                if filled:
                    score += 1
                else:
                    missing.append(label)
            product.pct_completeness = round(score / _TOTAL * 100, 1)
            product.pct_missing_fields = ', '.join(missing) if missing else ''
