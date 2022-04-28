from odoo import models, fields, api, _


class Partners(models.Model):
    _inherit = 'res.partner'

    projects_ids = fields.One2many('project_management.projects', 'clients_ids', string="Projects", readonly=True)