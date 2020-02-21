# -*- coding: utf-8 -*-

from odoo import models, fields


class hola(models.Model):
     _name = 'hola.usuarios'
     _description = 'esta clase almacena los usuarios'

     name = fields.Char()
     apellido = fields.Char()
     cedula = fields.Integer()
     matricula = fields.Float(compute="_value_pc", store=True)
     memo = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
