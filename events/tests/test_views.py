"""Tests for event CRUD views (US05, US06, US07)."""
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Event


User = get_user_model()


class EventListTests(TestCase):
    """Anyone can browse the upcoming events list (US07)."""

    def setUp(self):
        self.user = User.objects.create_user(username='org', password='pw')
        self.future = Event.objects.create(
            title='Sunrise yoga',
            description='Bring a mat.',
            starts_at=timezone.now() + timedelta(days=3),
            location='Riverside park',
            sport=Event.SPORT_YOGA,
            organiser=self.user,
        )
        self.past = Event.objects.create(
            title='Last week hike',
            description='Old event.',
            starts_at=timezone.now() - timedelta(days=7),
            location='Peak district',
            sport=Event.SPORT_HIKING,
            organiser=self.user,
        )

    def test_list_shows_only_upcoming(self):
        response = self.client.get(reverse('events:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sunrise yoga')
        self.assertNotContains(response, 'Last week hike')


class EventCreateTests(TestCase):
    """Logged-in users can create events (US05)."""

    def setUp(self):
        self.password = 'pw-Correct-Horse-9'
        self.user = User.objects.create_user(username='org', password=self.password)

    def test_anonymous_user_redirected_to_login(self):
        response = self.client.get(reverse('events:create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_authenticated_user_can_create_event(self):
        self.client.login(username='org', password=self.password)
        starts_at = (timezone.now() + timedelta(days=4)).replace(microsecond=0)
        response = self.client.post(
            reverse('events:create'),
            {
                'title': '5k run',
                'description': 'Easy pace.',
                'starts_at': starts_at.strftime('%Y-%m-%dT%H:%M'),
                'location': 'Common park',
                'sport': Event.SPORT_RUNNING,
            },
        )
        self.assertEqual(response.status_code, 302)
        event = Event.objects.get(title='5k run')
        self.assertEqual(event.organiser, self.user)


class EventEditDeleteTests(TestCase):
    """Organisers can edit and delete their own events; others cannot (US06)."""

    def setUp(self):
        self.password = 'pw-Correct-Horse-9'
        self.owner = User.objects.create_user(username='owner', password=self.password)
        self.other = User.objects.create_user(username='other', password=self.password)
        self.event = Event.objects.create(
            title='Original title',
            description='...',
            starts_at=timezone.now() + timedelta(days=2),
            location='Somewhere',
            sport=Event.SPORT_RUNNING,
            organiser=self.owner,
        )

    def test_owner_can_edit(self):
        self.client.login(username='owner', password=self.password)
        starts_at = self.event.starts_at.replace(microsecond=0)
        response = self.client.post(
            reverse('events:edit', args=[self.event.pk]),
            {
                'title': 'New title',
                'description': 'updated',
                'starts_at': starts_at.strftime('%Y-%m-%dT%H:%M'),
                'location': self.event.location,
                'sport': self.event.sport,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, 'New title')

    def test_non_owner_cannot_edit(self):
        self.client.login(username='other', password=self.password)
        response = self.client.get(reverse('events:edit', args=[self.event.pk]))
        self.assertEqual(response.status_code, 403)

    def test_owner_can_delete(self):
        self.client.login(username='owner', password=self.password)
        response = self.client.post(reverse('events:delete', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())

    def test_non_owner_cannot_delete(self):
        self.client.login(username='other', password=self.password)
        response = self.client.post(reverse('events:delete', args=[self.event.pk]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Event.objects.filter(pk=self.event.pk).exists())
