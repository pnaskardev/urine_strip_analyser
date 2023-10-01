from django.shortcuts import render
# from asgiref.sync import sync_to_async, async_to_sync
import asyncio
from django.views.generic.edit import CreateView

from . import forms
from . color_analyzer import analyse_colors

class UploadFileView(CreateView):
    form_class = forms.AnalyseForm
    template_name = 'analyse/home.html'

    def form_valid(self, form):
        instance = form.save()
        image_path = instance.image.path
        res = asyncio.run(analyse_colors(image_path))

        # Create a new empty form
        empty_form = forms.AnalyseForm()

        # Pass 'res', 'image_path', and 'empty_form' to the template context
        context = {'res': res, 'image': instance.image, 'form': empty_form}

        return render(self.request, 'analyse/home.html', context)
