"""Tests for the 24-hour reminder banner on the dashboard (US13)."""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Event, RSVP


User = get_user_model()


class DashboardRemindersTests(TestCase):

    def setUp(self):
        self.password = 'Zebra-Correct-Horse-9'
        self.user = User.objects.create_user(username='pat', password=self.password)
        self.organiser = User.objects.create_user(username='org', password=self.password)
        self.client.login(username='pat', password=self.password)

    def _make(self, title, hours_from_now):
        return Event.objects.create(
            title=title,
            description='...',
            starts_at=timezone.now() + timedelta(hours=hours_from_now),
            location='Loc',
            sport=Event.SPORT_RUNNING,
            organiser=self.organiser,
        )

    def test_banner_shown_for_attending_event_within_24h(self):
        soon = self._make('Soon session', hours_from_now=6)
        RSVP.objects.create(event=soon, user=self.user)
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, 'Reminder')
        self.assertContains(response, 'Soon session')

    def test_banner_not_shown_for_event_far_away(self):
        far = self._make('Next month session', hours_from_now=24 * 40)
        RSVP.objects.create(event=far, user=self.user)
        response = self.client.get(reverse('dashboard'))
        self.assertNotContains(response, 'Reminder')

    def test_banner_shown_for_own_organised_event_within_24h(self):
        soon = self._make('Own session', hours_from_now=3)
        soon.organiser = self.user
        soon.save()
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, 'Reminder')
        self.assertContains(response, 'Own session')
