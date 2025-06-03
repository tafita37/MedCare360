from odoo import models, fields

class MedicalConsultationRequestDetail(models.Model):
    _name = 'medical.consultation.request.symptom.rel'
    _description = 'Medical Consultation Request Detail'

    request_id = fields.Many2one('medical.consultation.request', string='Request', required=True)
    symptom_id = fields.Many2one('hospital.symptom', string='Symptom', required=True)
    severity_level_id = fields.Many2one('hospital.severity.level', string="Severity Level", required=True)