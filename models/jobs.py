from odoo import models, fields, api, _

class Jobs(models.Model):
    _name = 'project_management.jobs'
    _description = 'Jobs'

    name = fields.Char(string="Title", required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(default=fields.Date.today)
    workers_ids = fields.Many2many('hr.employee', string='Workers')
    projects_ids = fields.Many2one('project_management.projects', string='Projects')