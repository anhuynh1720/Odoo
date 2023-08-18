from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate property model"

    name = fields.Char()
