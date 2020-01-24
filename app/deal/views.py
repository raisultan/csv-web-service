import io
import csv

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from . import serializers
from core.models import Deal


class FileUploadAPIView(generics.CreateAPIView):
  serializer_class = serializers.FileUploadSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    file = serializer.validated_data['file']
    decoded_file = file.read().decode()
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string)
    for row in reader:
        try:
          deal = Deal(
            customer_name=row[0],
            item=row[1],
            total=row[2],
            quantity=row[3],
            date=row[4],
          )
          deal.save()
        except:
          #TODO: should raise proper exception
          pass
    return Response(status=status.HTTP_204_NO_CONTENT)
