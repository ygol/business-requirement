# © 2016-2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api


class BusinessRequirementConfigSettings(models.TransientModel):
    _name = "business.requirement.gap.task.config.setting"
    _inherit = "res.config.settings"

    gap_task_category_id = fields.Many2one(
        "project.task.type_id", string="Gap Analysis Task Category",
    )

    def set_business_requirement_gap_task_category_default(self):
        ir_values = self.env["ir.values"]
        gap_task_category_id = self.gap_task_category_id
        ir_values.set_default(
            "business.requirement.gap.task.config.setting",
            "gap_task_category_id",
            [gap_task_category_id.id] if gap_task_category_id else False,
            company_id=self.env.user.company_id.id,
        )

    @api.model
    def get_default_gap_task_category(self, fields):
        ir_vaules = self.env['ir.values']
        gap_task_category_id = None
        if 'gap_task_category_id' in fields:
            gap_task_category_id = ir_vaules.get_default(
                'business.requirement.gap.task.config.setting',
                'gap_task_category_id',
                company_id=self.env.user.company_id.id
            )
        return {'gap_task_category_id': gap_task_category_id}

    # def set_values(self):
    #     super(ResConfigSettings, self).set_values()
    #     select_type = self.env["ir.config_parameter"].sudo()
    #     select_type.set_param(
    #         "business.requirement.gap.task.config.setting.gap_task_category_id",
    #         self.gap_task_category_id,
    #     )

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     select_type = self.env["ir.config_parameter"].sudo()
    #     sell = select_type.get_param(
    #         "business.requirement.gap.task.config.setting.gap_task_category_id"
    #     )
    #     res.update({"gap_task_category_id": sell})

    # return res
