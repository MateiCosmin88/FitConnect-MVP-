from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    """Form for creating and editing an event."""

    class Meta:
        model = Event
        fields = ['title', 'description', 'starts_at', 'location', 'sport']
        widgets = {
            'starts_at': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['starts_at'].input_formats = ['%Y-%m-%dT%H:%M']
