from odoo import models, fields

class HospitalEfficiencyLevel(models.Model):
    _name = 'hospital.efficiency.level'
    _description = 'Efficiency Level'
    _order = "level asc"

    level = fields.Integer(string='Level', required=True, unique=True)
    name = fields.Char(string='Name', required=True, unique=True)
    description = fields.Char(string='Description', required=True, unique=True)