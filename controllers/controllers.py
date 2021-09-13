# -*- coding: utf-8 -*-
# from odoo import http


# class Phones(http.Controller):
#     @http.route('/phones/phones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phones/phones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phones.listing', {
#             'root': '/phones/phones',
#             'objects': http.request.env['phones.phones'].search([]),
#         })

#     @http.route('/phones/phones/objects/<model("phones.phones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phones.object', {
#             'object': obj
#         })
