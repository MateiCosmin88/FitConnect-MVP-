"""Tests for the Event model.

Written test-first (Sprint 2). The model does not exist yet.
"""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone


User = get_user_model()


class EventModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='org', password='pw')

    def _make_event(self, **overrides):
        from events.models import Event
        defaults = {
            'title': '6am parkrun',
            'description': 'Meet at the boathouse.',
            'starts_at': timezone.now() + timedelta(days=2),
            'location': 'Hyde Park',
            'sport': Event.SPORT_RUNNING,
            'organiser': self.user,
        }
        defaults.update(overrides)
        return Event.objects.create(**defaults)

    def test_can_create_event_with_required_fields(self):
        event = self._make_event()
        self.assertEqual(event.title, '6am parkrun')
        self.assertEqual(event.organiser, self.user)
        self.assertEqual(event.sport, 'running')

    def test_str_shows_title(self):
        event = self._make_event()
        self.assertEqual(str(event), '6am parkrun')

    def test_upcoming_manager_returns_only_future_events(self):
        from events.models import Event
        past = self._make_event(
            starts_at=timezone.now() - timedelta(days=1), title='Old event',
        )
        future = self._make_event(title='Tomorrow')
        upcoming = list(Event.objects.upcoming())
        self.assertIn(future, upcoming)
        self.assertNotIn(past, upcoming)

    def test_sport_choices_include_expected_options(self):
        from events.models import Event
        codes = {c[0] for c in Event.SPORT_CHOICES}
        self.assertTrue({'running', 'yoga', 'hiking', 'cycling'}.issubset(codes))
