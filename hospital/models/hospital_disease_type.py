from odoo import models, fields

class HospitalDiseaseType(models.Model):
    _name = 'hospital.disease.type'
    _description = 'Disease Type'
    _order = "name asc"

    name = fields.Char(string='Disease Type', required=True, unique=True)
    description = fields.Text(string='Description', required=True, unique=True)