# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import logging
from odoo import models, fields, api, _


_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    READONLY_STATES = {
        'purchase': [('readonly', True)],
        'done': [('readonly', True)],
        'cancel': [('readonly', True)],
    }

    dest_address_ref = fields.Char(
        string='Dropship reference',
        states=READONLY_STATES,
        help="Put an address if you want to deliver directly from the vendor to the customer. "
             "Otherwise, keep empty to deliver to your own company."
    )

    # def _prepare_purchase_order(self, product_id, product_qty, product_uom, origin, values, partner):
    #     return_values = super(PurchaseOrder, self)._prepare_purchase_order(product_id, product_qty, product_uom, origin, values, partner)
    #     return_values.update({'dest_address_ref': values.get('partner_dest_ref', False)})
    #     return return_values