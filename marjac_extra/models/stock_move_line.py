# -*- encoding: utf-8 -*-

from odoo import models,fields, api,tools
from odoo.exceptions import ValidationError


class StockMoveLineInherits(models.Model):
    _inherit = 'stock.move.line'

    
    unity_nbr = fields.Float(
        string="Nbr d'unité",
    )
    

    weight = fields.Float(
        string='Weight',
        compute='get_line_weight',
        store=True
    )

    @api.depends('move_id.weight')
    def get_line_weight(self):
        for rec in self:
            rec.weight = rec.move_id.weight