from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'project_management.wizard'
    _description = "Wizard: Quick Registration of Employees to Projects"

    def _default_projects(self):
        return self.env['project_management.projects'].browse(self._context.get('active'))

    projects_ids = fields.Many2many('project_management.projects',
        string="Projects", required=True, default=_default_projects)
    employee_ids = fields.Many2many('hr.employee', string="Employees")

    def subscribe(self):
        for project in self.projects_ids:
            project.employees_ids |= self.employee_ids
        return {}