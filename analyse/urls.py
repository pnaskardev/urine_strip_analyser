from django.urls import path
from . import views


urlpatterns = [
    path('analyse/', views.UploadFileView.as_view(), name='UploadFile'),
]