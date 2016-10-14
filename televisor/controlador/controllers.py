# -*- coding: utf-8 -*-
from openerp import http

# class televisor(http.Controller):
#     @http.route('/televisor/televisor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/televisor/televisor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('televisor.listing', {
#             'root': '/televisor/televisor',
#             'objects': http.request.env['televisor.televisor'].search([]),
#         })

#     @http.route('/televisor/televisor/objects/<model("televisor.televisor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('televisor.object', {
#             'object': obj
#         })
