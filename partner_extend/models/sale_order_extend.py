# -*- encoding: utf-8 -*-

from odoo import models,fields, api,tools
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    equipment_id = fields.Many2one(
        'maintenance.equipment',
        string='Équipement',
        )

    serial_num = fields.Char(string="N° de série",
                related="equipment_id.serial_no")

