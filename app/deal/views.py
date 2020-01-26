import io

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets, status

from . import serializers
from core.models import Item, Client, Deal
from .tasks import process_file
from .utils import create_most_valuable_clients_list


class FileUploadAPIView(generics.CreateAPIView):
  serializer_class = serializers.FileUploadSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    path = serializer.data['file'].split('localhost')[1]
    process_file.delay(path)

    return Response(status=status.HTTP_204_NO_CONTENT)


class MostValuableClientsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
  serializer_class = serializers.ClientSerializer
  queryset = create_most_valuable_clients_list(model=Client, attr='-spent_money')
