# -*- encoding: utf-8 -*-

from odoo import models,fields, api,tools
from odoo.exceptions import ValidationError


class StockMoveLineInherits(models.Model):
    _inherit = 'stock.move.line'

    
    unity_nbr = fields.Float(
        string="Nbr d'unité",
    )
    