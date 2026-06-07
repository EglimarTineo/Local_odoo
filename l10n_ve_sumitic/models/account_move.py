# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo.orm import Constraint

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

    constraints = [
        Constraint(
            'unique_control_number',
            'unique(l10n_ve_control_number, company_id, move_type)',
            'El número de control debe ser único por tipo de documento.'
        ),
    ]
