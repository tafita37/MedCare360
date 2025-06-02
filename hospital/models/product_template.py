from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'  # On hérite de la table existante

    expiration_date = fields.Date(string='Expiration Date', required=True)
    symptom_product_ids = fields.One2many(
        'hospital.symptom.product.rel',
        'product_id',
        string='Symptoms'
    )
    is_medication = fields.Boolean(
        string='Is Medication',
        default=True,
        readonly=True,
        help='Identifie si le produit est un médicament hospitalier.'
    )
    type = fields.Selection(required=False)
    categ_id = fields.Many2one(required=False)
