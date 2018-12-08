# -*- coding: utf-8 -*-

{
    'name': "mytranining",
    'summary': """
    课程培训模块，我的第一个odoo模块。""",
    'description':"""
    课程培训模块，我的第一个Odoo模块。""",
    'author': "老天",
    'website': "http://www.duuge.com",
    'category': "Tools",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_res_partner_views.xml',
        'views/tranining_views.xml'
    ],
    'demo':[
        
    ],
    'qweb':[
        
    ],
    'js':[
        
    ],
    'css':[
        
    ],
    'auto_install':'False',
    'application':'Ture',
}