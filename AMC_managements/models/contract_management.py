# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

class ContractManagement(models.Model):
    _name = 'contract.management'
    _description = 'Contract Management'

    name = fields.Char('Contract Name', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer Name', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    email = fields.Char('Email', related='customer_id.email', readonly=True)
    status = fields.Selection([
        ('new', 'New Contract'),
        ('expiring_soon', 'Expiring Soon'),
        ('active', 'Active')
    ], string='Status', compute='_compute_status', store=True)

    @api.depends('end_date')
    def _compute_status(self):
        for record in self:
            if record.end_date:
                days_remaining = (record.end_date - fields.Date.today()).days
                if days_remaining <= 10:
                    record.status = 'expiring_soon'
                else:
                    record.status = 'active'
            else:
                record.status = 'new'

    def send_email_reminder(self):
        if self.end_date and (self.end_date - fields.Date.today()).days <= 10:
            template = self.env.ref('AMC_managements.email_template_contract_expiry_reminder')
            template.send_mail(self.id, force_send=True)
        else:
            raise UserError('Contract is not expiring within the next 10 days.')