"""Tests for login and logout flows (US02, US03)."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class LoginTests(TestCase):
    """A returning user can log in with valid credentials (US02)."""

    def setUp(self):
        self.password = 'Zebra-Correct-Horse-9'
        self.user = User.objects.create_user(
            username='pat', password=self.password,
        )

    def test_login_page_renders_form(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_valid_login_redirects_to_home(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'pat', 'password': self.password},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.wsgi_request.user.username, 'pat',
        )

    def test_invalid_login_shows_error(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'pat', 'password': 'wrong'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class LogoutTests(TestCase):
    """A logged-in user can log out (US03)."""

    def setUp(self):
        self.password = 'Zebra-Correct-Horse-9'
        self.user = User.objects.create_user(
            username='pat', password=self.password,
        )
        self.client.login(username='pat', password=self.password)

    def test_logout_ends_session(self):
        response = self.client.post(reverse('logout'))
        self.assertIn(response.status_code, (200, 302))
        response = self.client.get(reverse('accounts:home'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
