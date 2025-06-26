from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MedicalConsultationRequest(models.Model):
    _name = 'medical.consultation.request'
    _description = 'Hospital Consultation Request'

    name = fields.Char(string='Fiche', readonly=True)
    patient_id = fields.Many2one(
        'hospital.patient', string='Patient', required=True, readonly=True, default=lambda self: self._get_default_patient()
    )
    nurse_id = fields.Many2one('hospital.nurse', string='Nurse')
    request_detail_ids = fields.One2many(
        'medical.consultation.request.symptom.rel',
        'request_id',
        string='Symptoms',
        required=True
    )

    @api.model
    def _get_default_patient(self):
        """
        Retourne le patient associé à l'utilisateur connecté.
        """
        current_user = self.env.user
        patient = self.env['hospital.patient'].search([('user_id', '=', current_user.id)], limit=1)
        if not patient:
            raise UserError(_("You must be logged in as a patient to create a request."))
        return patient.id

    @api.model
    def create(self, vals):
        # Call super to create the record and get the ID
        record = super(MedicalConsultationRequest, self).create(vals)
        # Set the name as "Fiche numéro <id>"
        record.name = "Fiche numéro %s" % record.id
        if record.request_detail_ids is None or len(record.request_detail_ids)==0 :
            raise UserError(_("You must add at least one symptom to the request."))
        return record