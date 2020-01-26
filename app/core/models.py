import os
import uuid
import datetime

from django.db import models


def csv_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/deals/', filename)

class DealHistoryFile(models.Model):
  file = models.FileField(upload_to=csv_file_path)

  def __str__(self):
    return f'{datetime.datetime.now()}'


class Item(models.Model):
  name = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.name


class Client(models.Model):
  username = models.CharField(max_length=255, unique=True)
  spent_money = models.IntegerField(default=0)
  gems = models.ManyToManyField(
    Item,
    related_name='clients',
    blank=True
  )

  def __str__(self):
    return self.username


class Deal(models.Model):
  client = models.ForeignKey(
    Client,
    on_delete=models.CASCADE,
    related_name='deals'
  )
  item = models.ForeignKey(
    Item,
    on_delete=models.CASCADE,
    related_name='deals'
  )
  total = models.IntegerField()
  quantity = models.IntegerField()
  date = models.DateTimeField()

  def __str__(self):
    return f'{self.date} {self.client} {self.item}'
