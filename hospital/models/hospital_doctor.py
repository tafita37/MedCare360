from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherits = {'res.users': 'user_id'}
    _description = 'Doctor'

    user_id = fields.Many2one('res.users', required=True, ondelete='cascade', string='User')
    specialty = fields.Char(string='Medical Specialty')