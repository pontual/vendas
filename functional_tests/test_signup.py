from django.urls import reverse

from .base import FunctionalTest


class SignupTest(FunctionalTest):

    def test_signup_link(self):
        self.browser.get(self.live_server_url)

        self.assertIn("Vendas", self.browser.title)

        signup_link = self.browser.find_element_by_id("link_signup")
        signup_link.click()

        self.wait_for(lambda: self.assertIn("Sign up", self.browser.title))


    def test_signup_as_selenium(self):
        signup_url = reverse('signup')
        self.browser.get(self.live_server_url + signup_url)
        
        username_input = self.browser.find_element_by_name("username")
        password1_input = self.browser.find_element_by_name("password1")
        password2_input = self.browser.find_element_by_name("password2")

        username_input.send_keys("selenium")
        password1_input.send_keys("secretpass123")
        password2_input.send_keys("secretpass123")

        submit_button = self.browser.find_element_by_id("submit_button")
        submit_button.click()
        
        self.wait_for(lambda: self.assertIn("Welcome back, selenium",
                                            self.browser.find_element_by_tag_name("body").text))
