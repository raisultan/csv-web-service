from rest_framework import serializers

from core.models import Item, Client


class FileUploadSerializer(serializers.Serializer):
  file = serializers.FileField()

  class Meta:
    fields = ('file', )


class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item
    fields = ('id', 'name')
    read_only_fields = ('id', )


class ClientSerializer(serializers.ModelSerializer):
  gems = ItemSerializer(many=True, read_only=True)

  class Meta:
    model = Client
    fields = ('id', 'username', 'spent_money', 'gems')
    read_only_fields = ('id', )
