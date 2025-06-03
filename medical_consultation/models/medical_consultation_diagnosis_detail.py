from odoo import models, fields

class MedicalConsultationDiagnosisDetail(models.Model):
    _name = 'medical.consultation.diagnosis.detail'
    _description = 'Medical Consultation Diagnosis Detail'

    diagnosis_id = fields.Many2one('medical.consultation.diagnosis', string='Diagnosis', required=True)
    medication_id = fields.Many2one('hospital.medication', string='Medication', required=True)
    quantity = fields.Float(string='Quantity', required=True)