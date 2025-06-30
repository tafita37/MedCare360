from odoo import models, fields

class Consultation(models.Model):
    _name = 'medical.consultation.consultation'
    _description = 'Medical Consultation Consultation'

    request_id = fields.Many2one('medical.consultation.request', string='Request', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('can_leave', 'Can Leave'),
            ('must_stay', 'Must Stay at Hospital'),
        ],
        string="State",
        default='new',
        readonly=True   
    )