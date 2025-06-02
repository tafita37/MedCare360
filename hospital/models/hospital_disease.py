from odoo import models, fields

class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'
    _order = "name asc"

    name = fields.Char(string='Symptom name', required=True, unique=True)
    disease_type_id = fields.Many2one('hospital.disease.type', string="Disease Type", required=True)
    description = fields.Text(string="Disease description", required=True, unique=True)
    is_contagious=fields.Boolean(string='Contagious ?', default=False, required=True)
    disease_symptom_id=fields.One2many('hospital.disease.symptom.rel', 'disease_id', string='Symptoms')