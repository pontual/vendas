# p. 251
import time

from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


User = get_user_model()
MAX_WAIT = 5


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn
    

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def login(self):
        user = User.objects.create_user(username="dummy", email="dummy@dummy.com", password="secret")
        self.browser.get(self.live_server_url + reverse('login'))

        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')

        username_field.send_keys("dummy")
        password_field.send_keys("secret")

        submit_button = self.browser.find_element_by_id('submit_button')
        submit_button.click()

        self.wait_for_text_in_body('Welcome back, dummy')


    @wait
    def wait_for(self, fn):
        # p. 256
        
        # Usage:
        # self.wait_for(lambda: self.assertEqual("My List",
        #               self.browser.find_element_by_tag_name('body').text))

        # p. 423 use @wait
        return fn()


    @wait
    def wait_for_text_in_title(self, text):
        self.assertIn(text, self.browser.title)

        
    @wait
    def wait_for_text_in_body(self, text):
        self.assertIn(text, self.browser.find_element_by_tag_name('body').text)
