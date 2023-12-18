# -*- encoding: utf-8 -*-

from odoo import models,fields, api,tools
from odoo.exceptions import ValidationError


class StockMoveLineInherits(models.Model):
    _inherit = 'stock.move.line'

    
    unity_nbr = fields.Float(
        string="Nbr d'unité",
    )
    

    weight = fields.Float(
        string='Poids',
        compute='get_line_weight',
    )

    @api.depends('product_id.weight', 'qty_done')
    def get_line_weight(self):
        for rec in self:
            rec.weight = rec.product_id.weight * rec.qty_done