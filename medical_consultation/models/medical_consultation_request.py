from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo import SUPERUSER_ID

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
    consultation_ids = fields.One2many(
        'medical.consultation.consultation',
        'request_id',
        string='Consultations'
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

    def open_affectation_wizard(self):
        self.ensure_one()
        return {
            'name': 'Affectation',
            'type': 'ir.actions.act_window',
            'res_model': 'medical.consultation.affectation.nurse.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref(
                'medical_consultation.view_affectation_wizard_nurse_form'
            ).id,
            'target': 'new',
            'context': {
                'default_request_id': self.id,
            },
        }


    def open_affectation_doctor_wizard(self):
        self.ensure_one()
        return {
            'name': 'Affectation',
            'type': 'ir.actions.act_window',
            'res_model': 'medical.consultation.affectation.doctor.wizard',
            'view_mode': 'form',
            'target': 'new',  
            'context': {
                'default_request_id': self.id,
            },
        }

    @api.model
    def search(self, args, offset=0, limit=None, order=None):
        user = self.env.user
        if self.env.is_superuser():
            return super().search(args, offset=offset, limit=limit, order=order)
        # Si l'utilisateur est infirmier
        if user.has_group('hospital.group_nurse'):
            nurse = self.env['hospital.nurse'].search([('user_id', '=', user.id)], limit=1)
            if nurse:
                args = args + [('nurse_id', '=', nurse.id)]
            else:
                args = args + [('nurse_id', '=', False)]  # Aucun résultat si pas d'infirmier lié
        # Si l'utilisateur est patient
        elif user.has_group('hospital.group_patient'):
            patient = self.env['hospital.patient'].search([('user_id', '=', user.id)], limit=1)
            if patient:
                args = args + [('patient_id', '=', patient.id)]
            else:
                args = args + [('patient_id', '=', False)]  # Aucun résultat si pas de patient lié
        return super().search(args, offset=offset, limit=limit, order=order)
