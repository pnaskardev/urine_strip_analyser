from django import forms

from .models import ImageModel

class AnalyseForm(forms.ModelForm):
    image=forms.ImageField(
        label='Upload Image',
        help_text='max. 42 megabytes'
    )

    class Meta:
        model=ImageModel
        fields = ['image']
        