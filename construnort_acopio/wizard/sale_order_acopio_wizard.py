from odoo import models, fields, api, _

class SaleOrderAcopioWizard(models.TransientModel):
    _name = 'sale.order.acopio.wizard'
    _description = 'Wizard para confirmar acopio en pedido de venta'

    sale_order_id = fields.Many2one('sale.order', string='Pedido de Venta', required=True, readonly=True)
    confirm_acopio = fields.Boolean('Confirmar acopio', required=True)

    def action_confirm_acopio(self):
        self.ensure_one()
        if self.confirm_acopio:
            self.sale_order_id.state = 'acopio'
        return {'type': 'ir.actions.act_window_close'}
