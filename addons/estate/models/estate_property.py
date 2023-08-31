from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char()
    bedroom = fields.Integer(default=2)
    availability_date = fields.Date(default=lambda self: fields.Date.today())
