from django.urls import path

from . import views


app_name = 'deal'

urlpatterns = [
  path('upload/', views.FileUploadAPIView.as_view()),
  path('clients/', views.MostValuableClientsListView.as_view()),
]
