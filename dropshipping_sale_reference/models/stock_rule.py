# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from odoo import models, fields, api, _


_logger = logging.getLogger(__name__)


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _prepare_purchase_order(self, company_id, origins, values):
        return_values = super(StockRule, self)._prepare_purchase_order(company_id, origins, values)
        values = values[0]
        return_values.update({'dest_address_ref': values.get('dest_address_ref', False)})
        return return_values