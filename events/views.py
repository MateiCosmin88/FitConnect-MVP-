"""Event views for Sprint 2 CRUD and Sprint 3 RSVP stories."""
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import EventForm
from .models import Event, RSVP
from .notifications import send_rsvp_confirmation


def event_list(request):
    """List upcoming events (US07)."""
    events = Event.objects.upcoming()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'events/event_list.html', {'events': page, 'page': page})


@login_required
def dashboard(request):
    """User dashboard with organised events, RSVPs and 24h reminders (US08, US13)."""
    organised = Event.objects.upcoming().filter(organiser=request.user)
    attending = Event.objects.upcoming().filter(rsvps__user=request.user)

    horizon = timezone.now() + timedelta(hours=24)
    reminders = (
        Event.objects.upcoming()
        .filter(starts_at__lte=horizon)
        .filter(Q(organiser=request.user) | Q(rsvps__user=request.user))
        .distinct()
    )

    return render(request, 'events/dashboard.html', {
        'organised': organised,
        'attending': attending,
        'reminders': reminders,
    })


@login_required
@require_POST
def rsvp(request, pk):
    """RSVP to an event (US09). Idempotent."""
    event = get_object_or_404(Event, pk=pk)
    obj, created = RSVP.objects.get_or_create(event=event, user=request.user)
    if created:
        send_rsvp_confirmation(obj)
    return redirect('events:detail', pk=event.pk)


@login_required
@require_POST
def cancel_rsvp(request, pk):
    """Cancel a previously created RSVP (US10)."""
    event = get_object_or_404(Event, pk=pk)
    RSVP.objects.filter(event=event, user=request.user).delete()
    return redirect('events:detail', pk=event.pk)


@login_required
def attendees(request, pk):
    """Show the attendee list – organiser only (US11)."""
    event = get_object_or_404(Event, pk=pk)
    if event.organiser_id != request.user.id:
        raise PermissionDenied('Only the organiser can view attendees.')
    return render(request, 'events/attendees.html', {
        'event': event,
        'attendees': event.attendees,
    })


def event_detail(request, pk):
    """Show a single event (helper for later stories)."""
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def event_create(request):
    """Create an event (US05)."""
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user
            event.save()
            return redirect('events:detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'mode': 'create'})


def _get_owned_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.organiser_id != request.user.id:
        raise PermissionDenied('Only the organiser can modify this event.')
    return event


@login_required
def event_edit(request, pk):
    """Edit an event owned by the current user (US06)."""
    event = _get_owned_event(request, pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'mode': 'edit', 'event': event})


@login_required
def event_delete(request, pk):
    """Delete an event owned by the current user (US06)."""
    event = _get_owned_event(request, pk)
    if request.method == 'POST':
        event.delete()
        return redirect('events:list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
