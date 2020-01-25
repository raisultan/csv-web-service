import io
import csv

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets, status

from . import serializers
from core.models import Item, Client, Deal
from .utils import check_deal_validity, check_item_existence_for_client, create_most_valuable_clients_list


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
      if check_deal_validity(row):
        try:
          Client.objects.get(username=row[0])
        except ObjectDoesNotExist:
          client = Client(username=row[0])
          client.save()

        try:
          Item.objects.get(name=row[1])
        except ObjectDoesNotExist:
          item = Item(name=row[1])
          item.save()

        #TODO: consider adding try/except
        deal = Deal(
          client=Client.objects.get(username=row[0]),
          item=Item.objects.get(name=row[1]),
          total=row[2],
          quantity=row[3],
          date=row[4],
        )
        deal.save()
        Client.objects.filter(username=deal.client).update(spent_money=F('spent_money') + deal.total)
        if check_item_existence_for_client(
          client=deal.client,
          item=deal.item
        ):
          pass
        else:
          deal.client.gems.add(deal.item)

    return Response(status=status.HTTP_204_NO_CONTENT)


class MostValuableClientsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
  serializer_class = serializers.ClientSerializer
  queryset = create_most_valuable_clients_list(model=Client, attr='-spent_money')
