from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherits = {'res.users': 'user_id'}
    _description = 'Patient'

    user_id = fields.Many2one('res.users', required=True, string='User')