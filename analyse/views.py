from django.shortcuts import render
# from asgiref.sync import sync_to_async, async_to_sync
import asyncio
from django.views.generic.edit import CreateView

from . import forms
from . color_analyzer import analyse_colors


def home(request):
    return render(request, 'analyse/home.html')


# def UploadFile(request):
#     if request.method == 'POST':
#         form = forms.AnalyseForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save()
#             image_path = instance.image.path
#             # res = async_to_sync(analyse_colors(image_path))
#             res = asyncio.run(analyse_colors(image_path))
#             print(res)
#             return HttpResponse('The file is saved')
#     else:
#         form = forms.AnalyseForm()
#     context = {'form': form, }
#     return render(request, 'upload.html', context)


class UploadFileView(CreateView):
    form_class = forms.AnalyseForm
    template_name = 'analyse/upload.html'

    def form_valid(self, form):
        instance = form.save()
        image_path = instance.image.path
        res = asyncio.run(analyse_colors(image_path))

        # Create a new empty form
        empty_form = forms.AnalyseForm()

        # Pass 'res', 'image_path', and 'empty_form' to the template context
        context = {'res': res, 'image': instance.image, 'form': empty_form}

        return render(self.request, 'analyse/upload.html', context)
