# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one(
            comodel_name='phones.manufacturer',
            ondelete='cascade',
            string='Manufacturer',
            required=True
    )

    model_id = fields.Many2one(
        comodel_name='phones.brand',
        string='Model',
        domain="[('manufacturer_id', '=', manufacturer_id)]",
    )

    # @api.onchange('manufacturer_id')
    # def onchange_manufacturer_id(self):
    #     for record in self:
    #         return {'domain': {'brand_id': [('manufacturer_id', '=', record.manufacturer_id.id)]}}

    @api.onchange('manufacturer_id')
    def _onchange_manufacturer_id(self):
        if self.model_id and self.model_id.manufacturer_id != self.manufacturer_id:
            self.model_id = None


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
