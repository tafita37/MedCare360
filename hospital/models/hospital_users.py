from odoo import models, api

class HospitalUsers(models.Model):
    _inherit = 'res.users'

    def _create_related_hospital_records(self):
        # Obtenez les IDs des groupes
        nurse_group_id = self.env.ref('hospital.group_nurse').id
        doctor_group_id = self.env.ref('hospital.group_doctor').id
        patient_group_id = self.env.ref('hospital.group_patient').id

        for user in self:
            group_ids = set(user.groups_id.ids)

            if nurse_group_id in group_ids:
                self.env['hospital.nurse'].sudo().search([('user_id', '=', user.id)]).unlink()
                self.env['hospital.nurse'].create({'user_id': user.id})

            if doctor_group_id in group_ids:
                self.env['hospital.doctor'].sudo().search([('user_id', '=', user.id)]).unlink()
                self.env['hospital.doctor'].create({'user_id': user.id})

            if patient_group_id in group_ids:
                self.env['hospital.patient'].sudo().search([('user_id', '=', user.id)]).unlink()
                self.env['hospital.patient'].create({'user_id': user.id})

    @api.model_create_multi
    def create(self, vals_list):
        users = super().create(vals_list)
        users._create_related_hospital_records()
        return users

    def write(self, vals):
        res = super().write(vals)
        if 'groups_id' in vals:
            self._create_related_hospital_records()
        return res
