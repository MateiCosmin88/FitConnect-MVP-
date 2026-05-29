from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """Sign-up form used by the registration view.

    Uses Django's built-in UserCreationForm; kept as a subclass so extra
    fields (email, first name) can be added later without changing the view.
    """

    class Meta(UserCreationForm.Meta):
        pass
