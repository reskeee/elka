from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'email', 'message']

    user = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Почта',
    }))

    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Сообщение',
    }))