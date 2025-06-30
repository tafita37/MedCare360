from odoo import models, fields, api

class AffectationDoctorWizard(models.TransientModel):
    _name = 'medical.consultation.affectation.doctor.wizard'
    _description = 'Wizard for affectation'

    request_id = fields.Many2one('medical.consultation.request', required=True, readonly=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)

    def action_confirm_affectation(self):
        self.ensure_one()
        self.env['medical.consultation.consultation'].create({
            'request_id': self.request_id.id,
            'doctor_id': self.doctor_id.id,
        })
        return {'type': 'ir.actions.act_window_close'}