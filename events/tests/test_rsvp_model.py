"""Tests for the RSVP model (US09)."""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone

from events.models import Event


User = get_user_model()


class RSVPModelTests(TestCase):

    def setUp(self):
        self.organiser = User.objects.create_user(username='org', password='pw')
        self.attendee = User.objects.create_user(username='att', password='pw')
        self.event = Event.objects.create(
            title='Trail run',
            description='...',
            starts_at=timezone.now() + timedelta(days=2),
            location='Woods',
            sport=Event.SPORT_RUNNING,
            organiser=self.organiser,
        )

    def test_create_rsvp(self):
        from events.models import RSVP
        rsvp = RSVP.objects.create(event=self.event, user=self.attendee)
        self.assertIsNotNone(rsvp.created_at)

    def test_user_can_only_rsvp_once_per_event(self):
        from events.models import RSVP
        RSVP.objects.create(event=self.event, user=self.attendee)
        with self.assertRaises(IntegrityError):
            RSVP.objects.create(event=self.event, user=self.attendee)

    def test_event_exposes_attendees(self):
        from events.models import RSVP
        RSVP.objects.create(event=self.event, user=self.attendee)
        self.assertIn(self.attendee, list(self.event.attendees))
