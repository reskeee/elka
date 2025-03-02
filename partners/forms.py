from django import forms
from django.forms import inlineformset_factory
from .models import Partners, PartnersImage


class PartnersForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ['name', 'description', 'main_image']


PartnersImageFormSet = inlineformset_factory(
    Partners,
    PartnersImage,
    fields=('image',),
    extra=5,
    can_delete=True,
    max_num=100,
)