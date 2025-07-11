from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Consultation(models.Model):
    _name = 'medical.consultation.consultation'
    _description = 'Medical Consultation Consultation'

    name = fields.Char(string='Consultation', readonly=True)
    request_id = fields.Many2one('medical.consultation.request', string='Request', required=True, unique=True)
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
    
    @api.model
    def create(self, vals):
        record = super(Consultation, self).create(vals)
        record.name = "Consultation numéro %s" % record.id
        return record