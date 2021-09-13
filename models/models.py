# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class phones(models.Model):
#     _name = 'phones.phones'
#     _description = 'phones.phones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api


class Manufacturer(models.Model):
    _name = 'phones.manufacturer'
#   _inherit = 'product.product'

    manufacturer_name = fields.Char(string='Manufacturer', required=True)


class Brand(models.Model):
    _name = 'phones.brand'
#    _inherit = 'product.product'

    brand_name = fields.Char(string='Brand', required=True)
    manufacturer_id = fields.Many2one(
        comodel_name='manufacturer',
        ondelete='cascade',
        string='Manufacturer',
        required=True
    )
