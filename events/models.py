"""Event model — Sprint 2, US05.

Represents a fitness meet-up organised by a user. Kept intentionally small
for the MVP; capacity and RSVP relations are added in Sprint 3.
"""
from django.conf import settings
from django.db import models
from django.utils import timezone


class EventQuerySet(models.QuerySet):

    def upcoming(self):
        return self.filter(starts_at__gte=timezone.now()).order_by('starts_at')


class Event(models.Model):
    SPORT_RUNNING = 'running'
    SPORT_YOGA = 'yoga'
    SPORT_HIKING = 'hiking'
    SPORT_CYCLING = 'cycling'
    SPORT_OTHER = 'other'
    SPORT_CHOICES = [
        (SPORT_RUNNING, 'Running'),
        (SPORT_YOGA, 'Yoga'),
        (SPORT_HIKING, 'Hiking'),
        (SPORT_CYCLING, 'Cycling'),
        (SPORT_OTHER, 'Other'),
    ]

    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    location = models.CharField(max_length=200)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default=SPORT_OTHER)
    organiser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organised_events',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = EventQuerySet.as_manager()

    class Meta:
        ordering = ['starts_at']

    def __str__(self):
        return self.title
