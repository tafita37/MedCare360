from odoo import models, fields

class HospitalSymptomMedicationRel(models.Model):
    _name = 'hospital.symptom.medication.rel'
    _description = 'Symptom Medication Relation'

    _sql_constraints = [
        (
            'check_symptom_medication_unique',  # nom interne
            'unique(symptom_id, medication_id)',      # contrainte SQL
            'The combination of symptom and medication must be unique !'  # message d'erreur
        ),
    ]

    symptom_id = fields.Many2one('hospital.symptom', string='Symptom', required=True)
    medication_id = fields.Many2one('hospital.medication', string='Medication', required=True)
    efficiency_level_id = fields.Many2one('hospital.efficiency.level', string="Efficiency Level", required=True)