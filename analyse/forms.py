from django import forms

from .models import ImageModel

class AnalyseForm(forms.ModelForm):
    image=forms.ImageField(
        label='Upload Image',
    )

    class Meta:
        model=ImageModel
        fields = ['image']
        