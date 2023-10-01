from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='analyse-home'),
    # path('UploadFile/', views.UploadFile, name='UploadFile'),
    path('UploadFile/', views.UploadFileView.as_view(), name='UploadFile'),
]