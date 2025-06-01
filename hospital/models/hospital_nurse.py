from odoo import models, fields

class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _inherits = {'res.users': 'user_id'}
    _description = 'Nurse'

    user_id = fields.Many2one('res.users', required=True, ondelete='cascade', string='User')