# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

 
class televisor(osv.osv):
     _name = 'televisor.televisor'
     _rec_name='modelo'
     
     _columns={
        'marca':fields.char('Marca del Tv',size=50,required=True,help='Marca del televisor'),
        'modelo':fields.char('Modelo del Tv',size=50,required=True,help='modelo de televisor'),
        'tamano':fields.char('Pulgadas del Tv',size=20,required=True,help='tamaño del televisor'),
        'color':fields.char('Color del Tv',size=20,required=True,help='color del televisor'),
        'precio':fields.char('Precio del TV',size=500,help='precio del televisor'),
        'fecha_p':fields.date('Fecha de Pedido',size=20,required=True,help='Fecha del pedido'),
        'active':fields.boolean('Activar Cliente',help='Si esta activo el motor lo incluira en la vista...')
        }
        
     _defaults={
        'active':True,
        }
     
