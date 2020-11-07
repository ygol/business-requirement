# Copyright 2020 Yves Goldberg (Ygol InternetWork)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class StakeholderRole(models.Model):

    _name = 'stakeholder.role'
    _description = 'Stakeholder Role'  # TODO

    name = fields.Char("Name", required=True)
