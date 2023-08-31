from odoo import http


class ContactController(http.Controller):
    @http.route('/contact/test', type='http', auth='none', methods=['GET'], cors='*')
    def contact_test(self, **kwargs):
        phone_number = kwargs.get('phoneNumber')
        display_name = kwargs.get('displayName')

        contact_list = http.request.env['res.users']
        contact_list = contact_list.search([])

        print(contact_list.read(['company_id', 'partner_id']))
