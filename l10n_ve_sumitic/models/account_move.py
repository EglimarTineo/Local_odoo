# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_ve_control_number = fields.Char(
        string='Número de Control',
        copy=False,
        help="Número de control del formato impreso (SENIAT)"
    )

    l10n_ve_taxpayer_type = fields.Selection([
        ('formal', 'Formal'),
        ('special', 'Especial'),
        ('ordinary', 'Ordinario'),
    ], string="Tipo de Contribuyente", store=True)
