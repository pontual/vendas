from django.urls import reverse

from .base import FunctionalTest

from companies.models import Company


class CompanyTest(FunctionalTest):

    def test_company_list_requires_login(self):
        self.browser.get(self.live_server_url + reverse('companies:list'))
        self.wait_for_text_in_body('Log in')
    
    
    def test_company_list_homepage(self):
        self.login()
        self.browser.get(self.live_server_url + reverse('companies:list'))
        self.wait_for_text_in_body('Company List')


    def test_new_company_appears_in_list(self):
        self.login()
        company = Company.objects.create(business_name="Acme Gears")
        self.browser.get(self.live_server_url + reverse('companies:list'))
        self.wait_for_text_in_body('Acme Gears')


    def test_get_new_company_form(self):
        self.login()
        self.browser.get(self.live_server_url + reverse('companies:new'))
        self.wait_for_text_in_body('Add/Edit Company')


    def test_new_company_from_form_appears_in_list(self):
        self.login()
        self.browser.get(self.live_server_url + reverse('companies:new'))
        self.wait_for_text_in_body('Add/Edit Company')

        business_name_field = self.browser.find_element_by_name('business_name')
        business_name_field.send_keys("A new company")

        submit_button = self.browser.find_element_by_id('submit_button')
        submit_button.click()

        self.wait_for_text_in_body("Company Details")
        self.wait_for_text_in_body("A new company")

        
