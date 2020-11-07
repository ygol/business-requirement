# Copyright 2020 Yves Goldberg (Ygol InternetWork)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class BusinessRequirementDeliverable(models.Model):

    _inherit = 'business.requirement.deliverable'

    stakeholder_role = fields.Many2one(
        comodel_name="stakeholder.role", string="Stakeholder Role"
    )
