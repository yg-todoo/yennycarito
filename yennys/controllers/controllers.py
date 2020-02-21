# -*- coding: utf-8 -*-
# from odoo import http


# class Yennys(http.Controller):
#     @http.route('/yennys/yennys/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yennys/yennys/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yennys.listing', {
#             'root': '/yennys/yennys',
#             'objects': http.request.env['yennys.yennys'].search([]),
#         })

#     @http.route('/yennys/yennys/objects/<model("yennys.yennys"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yennys.object', {
#             'object': obj
#         })
