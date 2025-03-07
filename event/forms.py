from .models import Events
from django import forms

class NewItemForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ['title', 'description', 'image', 'event_datetime', 'status', 'latitude', 'longitude', 'address']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'image': forms.ClearableFileInput(),
            'event_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'address': forms.HiddenInput(),
        }


class EditItemForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ['title', 'description', 'image', 'event_datetime', 'status', 'latitude', 'longitude', 'address']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'image': forms.ClearableFileInput(),
            'event_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'address': forms.HiddenInput(),
        }