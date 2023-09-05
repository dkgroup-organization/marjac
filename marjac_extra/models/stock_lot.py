# -*- encoding: utf-8 -*-

from odoo import models,fields, api,tools
from odoo.exceptions import ValidationError


class StockLotInherits(models.Model):
    _inherit = 'stock.lot'

    
    fabrication_date = fields.Date(string='Date de fabrication')
    