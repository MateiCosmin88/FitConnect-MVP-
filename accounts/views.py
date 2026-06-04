from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


def placeholder_home(request):
    return render(request, 'accounts/placeholder_home.html')


@login_required
def profile(request):
    """Show the logged-in user's details (US04)."""
    return render(request, 'accounts/profile.html', {'user_obj': request.user})


class RegisterView(CreateView):
    """User registration view (US01).

    On success the newly created user is logged in and redirected to the
    home page.
    """

    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:home')
