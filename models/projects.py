from odoo import models, fields, api, _, exceptions

class Projects(models.Model):
    _name = 'project_management.projects'
    _description = 'Projects'

    name = fields.Char(string=_("Title"), required=True)
    description = fields.Text(string=_("Description"))
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(default=fields.Date.today)
    clients_ids = fields.Many2one('res.partner', string=_('Clients'))
    manager_ids = fields.Many2one('hr.employee', string=_('Manager'), domain=[('manager', '=', True)])
    employees_ids = fields.Many2many('hr.employee', string=_('Employee'))
    employees_count = fields.Integer(string=_('Employees count'), compute='_get_employees_count', store=True)
    jobs_ids = fields.One2many('project_management.jobs', 'projects_ids', string=_('Jobs'))
    invoices_ids = fields.One2many('project_management.invoices', 'projects_ids', string=_('Invoices'))
    max_workers = fields.Integer(string=_('Maximum workers'))
    min_workers = fields.Integer(string=_('Minimum workers'))
    workers = fields.Float(string=_('Working %'), compute='_working')
    duration = fields.Integer(string=_('Duration'), compute='_duration')
    color = fields.Integer()
    active = fields.Boolean(default=True)

    @api.depends('employees_ids')
    def _get_employees_count(self):
        for r in self:
            r.employees_count = len(r.employees_ids)

    @api.depends('end_date', 'start_date')
    def _duration(self):
        for r in self:
            r.duration = abs((r.end_date - r.start_date).days)

    @api.depends('max_workers', 'employees_ids')
    def _working(self):
        for record in self:
            if not record.max_workers:
                record.workers = 0
            else:
                record.workers = (len(record.employees_ids) / record.max_workers) * 100

    @api.constrains('manager_ids', 'employees_ids')
    def _check_managers_not_in_workers(self):
        for record in self:
            if record.manager_ids and record.manager_ids in record.employees_ids:
                raise exceptions.ValidationError("A manager cannot be a worker")

    @api.constrains('employees_ids', 'max_workers', 'min_workers')
    def _worker_limits(self):
        for r in self:
            if len(r.employees_ids) > r.max_workers:
                raise exceptions.ValidationError("Too many workers")
            elif len(r.employees_ids) < r.min_workers:
                raise exceptions.ValidationError("Too few workers")