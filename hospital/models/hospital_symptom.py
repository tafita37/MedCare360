from odoo import models, fields

class HospitalSymptom(models.Model):
    _name = 'hospital.symptom'
    _description = 'Symptom'
    _order = "name asc"

    name = fields.Char(string='Symptom name', required=True, unique=True)
    description = fields.Text(string='Description', required=True, unique=True)