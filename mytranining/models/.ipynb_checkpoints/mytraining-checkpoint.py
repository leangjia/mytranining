# -*- coding:utf-8 -*-

from odoo import api, fields, models

class Mytraining(models,Model):
    _name = 'mytraining'
    _desription = '培训'
    
    name = fields.Chart(String='名称')