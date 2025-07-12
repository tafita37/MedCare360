from odoo import models, fields

class HospitalNurse(models.Model):
    _inherit = 'hospital.nurse'

    request_count = fields.Integer(
        string="Requests To Do",
        compute='_compute_request_count'
    )

    def _compute_request_count(self):
        consultationRequest = self.env['medical.consultation.request']
        consultation = self.env['medical.consultation.consultation']
        for nurse in self:
            # Cherche les requests où nurse_id = nurse.id
            requests = consultationRequest.search([('nurse_id', '=', nurse.id)])
            # Filtre celles qui n'ont pas encore de consultation liée
            count = 0
            for req in requests:
                has_consult = consultation.search_count([('request_id', '=', req.id)])
                if not has_consult:
                    count += 1
            nurse.request_count = count