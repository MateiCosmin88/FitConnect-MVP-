from django.shortcuts import render


def placeholder_home(request):
    """Temporary landing until the events app provides the real home view."""
    return render(request, 'accounts/placeholder_home.html')
