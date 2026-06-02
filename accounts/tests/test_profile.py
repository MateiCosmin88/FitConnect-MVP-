"""Tests for the simple user profile page (US04)."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class ProfileViewTests(TestCase):

    def setUp(self):
        self.password = 'Zebra-Correct-Horse-9'
        self.user = User.objects.create_user(
            username='pat', email='pat@example.com', password=self.password,
        )

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_authenticated_user_sees_their_details(self):
        self.client.login(username='pat', password=self.password)
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pat')
        self.assertContains(response, 'pat@example.com')
