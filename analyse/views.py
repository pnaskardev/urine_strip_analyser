from django.shortcuts import render
import asyncio
from django.views.generic.edit import CreateView

from . import forms
from . color_analyzer import analyse_colors

# Define a class-based view named UploadFileView that inherits from CreateView
class UploadFileView(CreateView):
    # Specify the form class to be used for the view
    form_class = forms.AnalyseForm
    # Specify the template name to render the view
    template_name = 'analyse/home.html'

    # Define a method to handle a valid form submission
    def form_valid(self, form):
        # Save the form data as a new instance
        instance = form.save()
        # Get the path of the uploaded image
        image_path = instance.image.path
        # Analyze the colors in the image using asyncio
        res = asyncio.run(analyse_colors(image_path))

        # Create a new empty form for future submissions
        empty_form = forms.AnalyseForm()

        # Prepare the context to be passed to the template
        context = {
            'res': res,              # Result from color analysis
            'image': instance.image, # Uploaded image
            'form': empty_form       # Empty form for next submission
        }

        # Render the template with the updated context
        return render(self.request, 'analyse/home.html', context)