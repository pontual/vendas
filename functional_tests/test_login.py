from django.contrib.auth import get_user_model
from django.urls import reverse

from .base import FunctionalTest

User = get_user_model()


class LoginTest(FunctionalTest):

    def test_login(self):

        self.login()
