# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductInherit(models.Model):
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one(
            comodel_name='phones.manufacturer',
            ondelete='cascade',
            string='Manufacturer',
            required=True
    )
    brand_id = fields.Many2one(
        comodel_name='phones.brand',
        ondelete='cascade',
        string='Brand',
        required=True
    )

    @api.onchange('manufacturer_id')
    def onchange_manufacturer_id(self):
        for record in self:
            return {'domain': {'brand_id': [('manufacturer_id', '=', record.manufacturer_id.id)]}}


class Manufacturer(models.Model):
    _name = 'phones.manufacturer'
    _rec_name = 'manufacturer_name'

    manufacturer_name = fields.Char(string='Manufacturer', required=True)
    brand_ids = fields.One2many('phones.brand', 'manufacturer_id', string='Manufacturers')


class Brand(models.Model):
    _name = 'phones.brand'
    _rec_name = 'brand_name'

    brand_name = fields.Char(string='Brand', required=True)
    manufacturer_id = fields.Many2one(
        comodel_name='phones.manufacturer',
        ondelete='cascade',
        string='Manufacturer',
        required=True
    )
