from django.urls import path, include

from . import views


app_name = 'deal'

urlpatterns = [
  path('upload/', views.FileUploadAPIView.as_view()),
  path('clients/', views.MostValuableClientsViewSet.as_view({'get': 'list'})),
]
