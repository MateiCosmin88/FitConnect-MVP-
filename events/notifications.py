"""Email notification helpers (US12).

Kept in a dedicated module so future channels (SMS, push) can be added
alongside without touching the views.
"""
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_rsvp_confirmation(rsvp):
    """Send an email confirming an RSVP to the attendee."""
    if not rsvp.user.email:
        return
    context = {'rsvp': rsvp, 'event': rsvp.event, 'user': rsvp.user}
    subject = f'You are attending "{rsvp.event.title}"'
    body = render_to_string('events/emails/rsvp_confirmation.txt', context)
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[rsvp.user.email],
        fail_silently=False,
    )
