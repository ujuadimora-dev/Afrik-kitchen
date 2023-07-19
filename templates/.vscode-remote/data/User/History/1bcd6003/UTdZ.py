from django import forms
#from .forms import EventForm

class EventForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length=100)
    event_date = forms.DateField(label='Event Date')
    event_description = forms.CharField(label='Event Description', widget=forms.Textarea)
    # Add more fields as needed

    def clean_event_date(self):
        event_date = self.cleaned_data.get('event_date')
        # Add any custom validation or cleaning for the event_date field
        return event_date
