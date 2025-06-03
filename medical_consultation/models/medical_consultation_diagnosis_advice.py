from odoo import models, fields

class MedicalConsultationDiagnosisAdvice(models.Model):
    _name = 'medical.consultation.diagnosis.advice'
    _description = 'Medical Consultation Diagnosis Advice'

    diagnosis_id = fields.Many2one('medical.consultation.diagnosis', string='Diagnosis', required=True)
    advice_description = fields.Text(string='Advice', required=True)