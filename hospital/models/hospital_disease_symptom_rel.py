from odoo import models, fields

class HospitalDiseaseSymptomRel(models.Model):
    _name = 'hospital.disease.symptom.rel'
    _description = 'Disease-Symptom Relation'

    _sql_constraints = [
        (
            'check_disease_symptom_unique',  # nom interne
            'unique(disease_id, symptom_id)',      # contrainte SQL
            'The combination of disease and symptom must be unique !'  # message d'erreur
        ),
    ]

    name = fields.Char(string='Name', required=True, unique=True)
    disease_id = fields.Many2one('hospital.disease', string="Disease", required=True)
    symptom_id = fields.Many2one('hospital.symptom', string="Symptom", required=True)
    severity_level_id = fields.Many2one('hospital.severity.level', string="Severity Level", required=True)