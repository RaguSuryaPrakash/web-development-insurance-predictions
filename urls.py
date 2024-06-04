from django.urls import path
from .views import dataUploadView

app_name = 'insuApp'

urlpatterns = [
    path('upload/', dataUploadView.as_view(), name='upload'),
]
