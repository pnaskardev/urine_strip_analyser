from django import forms

from .models import ImageModel

# Define a form class named AnalyseForm that inherits from forms.ModelForm
class AnalyseForm(forms.ModelForm):
    # Create a form field named 'image' of type forms.ImageField
    image = forms.ImageField(
        label='Upload Image',  # Set the label for the field
    )

    # Define the form's metadata using the Meta inner class
    class Meta:
        model = ImageModel  # Associate the form with the ImageModel model
        fields = ['image']  # Specify the fields to include in the form