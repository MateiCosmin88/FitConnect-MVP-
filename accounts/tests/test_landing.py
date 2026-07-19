"""Tests for the public landing page (US16)."""
from django.test import TestCase
from django.urls import reverse


class LandingPageTests(TestCase):

    def test_landing_page_renders_for_anonymous(self):
        response = self.client.get(reverse('accounts:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'FitConnect')

    def test_landing_page_explains_value_proposition(self):
        response = self.client.get(reverse('accounts:home'))
        self.assertContains(response, 'meetups')
        self.assertContains(response, 'Sign up')
