from odoo import models, fields, api, _


class Employee(models.Model):
    _inherit = 'hr.employee'

    manager = fields.Boolean('Manager', default=False)
    projects_ids = fields.Many2many('project_management.projects', string="Projects", readonly=True)