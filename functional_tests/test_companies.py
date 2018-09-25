from django.urls import reverse

from .base import FunctionalTest

from companies.models import Company


class CompanyTest(FunctionalTest):

    def test_company_list_homepage(self):

        self.browser.get(self.live_server_url + reverse('companies:list'))

        self.wait_for_text_in_body('Company List')


    def test_new_company_appears_in_list(self):
        # create a company
        
        pass
