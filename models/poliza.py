# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoPoliza(models.Model):
    _name = 'seguros.tipo_poliza'

    name = fields.Char(string="Nombre", required=True)
    poliza_ids = fields.One2many(
        'seguros.poliza',  # related model
        'tipo_poliza_id',  # field for "this" on related model
        string='Polizas')

    total_poliza = fields.Integer(
        string="Total de polizas", compute="_total_poliza")

    @api.one
    def _total_poliza(self):
        self.total_poliza = len(self.poliza_ids)


class Poliza(models.Model):
    _name = 'seguros.poliza'

    name = fields.Char(string="Nombre", required=True)

    duration = fields.Integer(string="Plazo", required=True)
    cost = fields.Float(string="Prima")
    date_contract = fields.Date("Fecha de Contrato")

    tipo_poliza_id = fields.Many2one(
        'seguros.tipo_poliza', string="Tipo de Poliza")
