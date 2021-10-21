# -*- coding: utf-8 -*-


from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _compute_qty_received(self):
        super(PurchaseOrderLine, self)._compute_qty_received()
        print(">>>>>>", self.product_qty)
        if self.qty_received > 0:
            self.product_qty = self.qty_received
            print(">>>>>>", self.qty_received)
