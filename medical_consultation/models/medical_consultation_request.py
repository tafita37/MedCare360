from odoo import models, fields

class MedicalConsultationRequest(models.Model):
    _name = 'medical.consultation.request'
    _description = 'Hospital Consultation Request'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    nurse_id = fields.Many2one('hospital.nurse', string='Nurse')