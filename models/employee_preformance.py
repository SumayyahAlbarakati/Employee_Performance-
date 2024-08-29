from odoo import models, fields, api

class EmployeePerformance(models.Model):
    _name = 'employee.performance'
    _description = 'Employee Performance'

    employee_name = fields.Many2one('res.partner', string='Employee Name')
    review_date = fields.Date(string='Review Date')
    performance_rating = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
    ], string='Performance Rating')
    comments = fields.Text(string='Comments')
