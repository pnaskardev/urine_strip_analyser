from django.shortcuts import render
from django.shortcuts import render, HttpResponse

from . import forms


def home(request):
    return render(request, 'analyse/home.html')


def UploadFile(request):
    if request.method == 'POST':
        form = forms.AnalyseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = forms.AnalyseForm()
    context = {'form':form,}
    return render(request, 'upload.html', context)