from odoo import http


class ContactController(http.Controller):
    @http.route('/contact/test', type='http', auth='public', methods=['GET'], cors='*')
    def contact_test(self, **kwargs):
        phone_number = kwargs.get('phoneNumber')
        display_name = kwargs.get('displayName')

        contact_list = http.request.env['res.partner']
        contact_list = contact_list.sudo().search([('phone', '=', phone_number), ('display_name', '=', display_name)])

        print(phone_number)
        print(contact_list.read(['id', 'name', 'email', 'phone']))

        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'My Action Name',
        #     'view_mode': 'form',
        #     'res_model': 'res.partner',
        #     'res_id': contact_list.id,
        # }
