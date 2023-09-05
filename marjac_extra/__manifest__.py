# -*- coding: utf-8 -*-

{
    "name": "Ajout champs divers dans les livraisons et leurs rapports",
    "version": "1.0",
    "depends": ['base', 'sale', 'account', 'stock', 'product_expiry'],
    "author": "Mehdi Hajji",
    "summary": "Date de fabrication, Date d'expiration, Nbre d'unité etc...",
    'website': 'http://www.dkdigital.fr',
    "category": "BASE",
    "description": "Ajouter des infos sup",
    "init_xml": [],
    'data': [
        'views/report_delivery_document.xml',
        'views/stock_lot_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
