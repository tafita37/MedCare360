from odoo import models, fields

class HospitalSeverityLevel(models.Model):
    _name = 'hospital.severity.level'
    _description = 'Severity Level'
    _order = "level asc"

    level = fields.Integer(string='Level', required=True, unique=True)
    name = fields.Char(string='Name', required=True, unique=True)
    description = fields.Char(string='Description', required=True, unique=True)