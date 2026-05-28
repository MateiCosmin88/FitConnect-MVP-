"""Tests for user registration (US01).

Written test-first as part of the TDD cycle. When this file lands the
implementation does not yet exist and every test should fail.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class RegistrationViewTests(TestCase):
    """The register page is available and creates a user on valid POST."""

    url = None

    def setUp(self):
        self.url = reverse('accounts:register')

    def test_get_returns_registration_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password1"')
        self.assertContains(response, 'name="password2"')

    def test_valid_post_creates_user_and_redirects(self):
        response = self.client.post(
            self.url,
            {
                'username': 'sarah',
                'password1': 'zebra-Correct-Horse-9',
                'password2': 'zebra-Correct-Horse-9',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='sarah').exists())

    def test_invalid_post_shows_errors_and_does_not_create_user(self):
        response = self.client.post(
            self.url,
            {
                'username': 'sarah',
                'password1': 'abc',
                'password2': 'xyz',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='sarah').exists())
        self.assertContains(response, 'password')

    def test_new_user_is_logged_in_after_registration(self):
        self.client.post(
            self.url,
            {
                'username': 'alex',
                'password1': 'zebra-Correct-Horse-9',
                'password2': 'zebra-Correct-Horse-9',
            },
        )
        response = self.client.get(reverse('accounts:home'))
        self.assertEqual(response.wsgi_request.user.username, 'alex')
