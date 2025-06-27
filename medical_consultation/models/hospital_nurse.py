from odoo import models, fields

class HospitalNurse(models.Model):
    _inherit = 'hospital.nurse'
    _order = 'request_count desc'

    request_count = fields.Integer(
        string="Consultation Requests To Do",
        compute='_compute_request_count',
        store=True
    )

    def _compute_request_count(self):
        ConsultationRequest = self.env['medical.consultation.request']
        Consultation = self.env['medical.consultation.consultation']
        for nurse in self:
            # Cherche les requests où nurse_id = nurse.id
            requests = ConsultationRequest.search([('nurse_id', '=', nurse.id)])
            # Filtre celles qui n'ont pas encore de consultation liée
            count = 0
            for req in requests:
                has_consult = Consultation.search_count([('request_id', '=', req.id)])
                if not has_consult:
                    count += 1
            nurse.request_count = count