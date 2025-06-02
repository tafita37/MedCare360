from odoo import models, fields

class HospitalSymptomProductRel(models.Model):
    _name = 'hospital.symptom.product.rel'
    _description = 'Symptom Medication Relation'

    _sql_constraints = [
        (
            'check_symptom_medication_unique',  # nom interne
            'unique(symptom_id, product_id)',      # contrainte SQL
            'The combination of symptom and medication must be unique !'  # message d'erreur
        ),
    ]

    symptom_id = fields.Many2one('hospital.symptom', string='Symptom', required=True)
    product_id = fields.Many2one('product.template', string='Medication', required=True)
    efficiency_level_id = fields.Many2one('hospital.efficiency.level', string="Efficiency Level", required=True)