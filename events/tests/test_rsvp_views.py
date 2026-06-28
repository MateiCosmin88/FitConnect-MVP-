"""Tests for RSVP join, cancel and attendee list views (US09, US10, US11)."""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Event, RSVP


User = get_user_model()


class RSVPViewTests(TestCase):

    def setUp(self):
        self.password = 'Zebra-Correct-Horse-9'
        self.organiser = User.objects.create_user(
            username='org', email='org@example.com', password=self.password,
        )
        self.attendee = User.objects.create_user(
            username='att', email='att@example.com', password=self.password,
        )
        self.event = Event.objects.create(
            title='Beach yoga',
            description='...',
            starts_at=timezone.now() + timedelta(days=2),
            location='Beach',
            sport=Event.SPORT_YOGA,
            organiser=self.organiser,
        )

    # ----- Join -----

    def test_anonymous_cannot_join(self):
        response = self.client.post(reverse('events:rsvp', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_logged_in_user_can_join_event(self):
        self.client.login(username='att', password=self.password)
        response = self.client.post(reverse('events:rsvp', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(RSVP.objects.filter(event=self.event, user=self.attendee).exists())

    def test_joining_twice_is_idempotent(self):
        self.client.login(username='att', password=self.password)
        self.client.post(reverse('events:rsvp', args=[self.event.pk]))
        self.client.post(reverse('events:rsvp', args=[self.event.pk]))
        self.assertEqual(
            RSVP.objects.filter(event=self.event, user=self.attendee).count(), 1,
        )

    # ----- Cancel -----

    def test_user_can_cancel_rsvp(self):
        self.client.login(username='att', password=self.password)
        RSVP.objects.create(event=self.event, user=self.attendee)
        response = self.client.post(reverse('events:cancel_rsvp', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(RSVP.objects.filter(event=self.event, user=self.attendee).exists())

    # ----- Attendee list (organiser only) -----

    def test_organiser_sees_attendees(self):
        RSVP.objects.create(event=self.event, user=self.attendee)
        self.client.login(username='org', password=self.password)
        response = self.client.get(reverse('events:attendees', args=[self.event.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'att')

    def test_non_organiser_cannot_see_attendees(self):
        RSVP.objects.create(event=self.event, user=self.attendee)
        self.client.login(username='att', password=self.password)
        response = self.client.get(reverse('events:attendees', args=[self.event.pk]))
        self.assertEqual(response.status_code, 403)

    # ----- Email confirmation (US12) -----

    def test_email_sent_on_rsvp(self):
        self.client.login(username='att', password=self.password)
        self.client.post(reverse('events:rsvp', args=[self.event.pk]))
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertIn('Beach yoga', message.subject)
        self.assertIn('att@example.com', message.to)
