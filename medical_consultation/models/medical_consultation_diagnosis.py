from odoo import models, fields

class MedicalConsultationDiagnosis(models.Model):
    _name = 'medical.consultation.diagnosis'
    _description = 'Medical Consultation Diagnosis'
    
    consultation_id = fields.Many2one('medical.consultation.consultation', string='Consultation', required=True)
    disease_id = fields.Many2one('hospital.disease', string='Disease', required=True)