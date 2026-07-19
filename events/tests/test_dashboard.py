"""Tests for the personal dashboard (US08).

In Sprint 2 the dashboard lists the events the current user *organises*.
In Sprint 3 the same view will also list events the user has RSVP'd to.
"""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Event


User = get_user_model()


class DashboardTests(TestCase):

    def setUp(self):
        self.password = 'Zebra-Correct-Horse-9'
        self.user = User.objects.create_user(username='pat', password=self.password)
        self.other = User.objects.create_user(username='sam', password=self.password)

    def _make_event(self, title, organiser, days_from_now=1):
        return Event.objects.create(
            title=title,
            description='...',
            starts_at=timezone.now() + timedelta(days=days_from_now),
            location='Loc',
            sport=Event.SPORT_RUNNING,
            organiser=organiser,
        )

    def test_anonymous_user_redirected_to_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_shows_events_i_organise(self):
        mine = self._make_event('Mine', self.user)
        theirs = self._make_event('Theirs', self.other)
        self.client.login(username='pat', password=self.password)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mine')
        self.assertNotContains(response, 'Theirs')

    def test_only_upcoming_events(self):
        past = self._make_event('Old', self.user, days_from_now=-5)
        future = self._make_event('Soon', self.user, days_from_now=2)
        self.client.login(username='pat', password=self.password)
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, 'Soon')
        self.assertNotContains(response, 'Old')
