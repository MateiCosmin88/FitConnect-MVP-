"""Event views implementing the Sprint 2 CRUD stories."""
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm
from .models import Event


def event_list(request):
    """List upcoming events (US07)."""
    events = Event.objects.upcoming()
    return render(request, 'events/event_list.html', {'events': events})


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
