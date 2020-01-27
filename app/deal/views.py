from rest_framework.response import Response
from rest_framework import generics, status

from . import serializers
from core.models import Client
from .tasks import process_file


class FileUploadAPIView(generics.CreateAPIView):
  serializer_class = serializers.FileUploadSerializer

  def post(self, request, *args, **kwargs):
    if str(request.FILES['file']).endswith('.csv'):
      serializer = self.get_serializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        path = serializer.data['file'].split('localhost')[1]
        process_file.delay(path)

        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)


class MostValuableClientsListView(generics.ListAPIView):
  serializer_class = serializers.ClientSerializer
  queryset = Client.objects.all()

  def list(self, request, *args, **kwargs):
    if Client.objects.all().count() >= 5:
      clients = Client.objects.order_by('-spent_money')[:5]
    else:
      clients = Client.objects.order_by('-spent_money')

    result = []
    for client in clients:
      gems_filter_set = set()
      for other_client in clients:
        if other_client is not client:
          gems_filter_set.update(other_client.gems.all())
      result.append({
        'username': client.username,
        'spent_money': client.spent_money,
        'gems': client.gems.filter(name__in=gems_filter_set),
      })

    serializer = serializers.ClientSerializer(result, many=True)
    return Response(serializer.data)
