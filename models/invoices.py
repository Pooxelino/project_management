from odoo import models, fields, api, _

class Projects(models.Model):
    _name = 'project_management.invoices'
    _description = 'Invoices'

    name = fields.Char(string="Title", required=True)
    payment = fields.Float(string="Payment", required=True)
    clients_ids = fields.Many2many('res.partner', string='Clients')
    projects_ids = fields.Many2one('project_management.projects', string='Projects')
    # lines_ids = fields.One2many('project_management.projects', string='Projects')