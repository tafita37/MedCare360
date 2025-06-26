from odoo import models, fields, api

class AffectationNurseWizard(models.TransientModel):
    _name = 'medical.consultation.affectation.nurse.wizard'
    _description = 'Wizard pour affectation'

    request_id = fields.Many2one('medical.consultation.request', required=True, readonly=True)
    nurse_id = fields.Many2one('hospital.nurse', string='Infirmière', required=True)

    def action_confirm_affectation(self):
        self.ensure_one()
        self.request_id.write({'nurse_id': self.nurse_id.id})
        return {'type': 'ir.actions.act_window_close'}
