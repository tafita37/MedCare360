from odoo import models, fields

class HospitalMedication(models.Model):
    _name = 'hospital.medication'
    _description = 'Hospital Medication'

    commercial_name = fields.Char(string='Commercial Name', required=True, unique=True)
    description = fields.Text(string='Description', required=True, unique=True)
    price = fields.Float(string='Price', required=True)
    expiration_date = fields.Date(string='Expiration Date', required=True)