# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    taxpayer_type = fields.Selection([
        ('formal', 'Formal'),
        ('special', 'Especial'),
        ('ordinary', 'Ordinario'),
    ], string="Tipo de Contribuyente", default='ordinary')

    retention_iva_sequence_id = fields.Many2one(
        'ir.sequence', string="Secuencia de Retención IVA"
    )
    retention_islr_sequence_id = fields.Many2one(
        'ir.sequence', string="Secuencia de Retención ISLR"
    )
