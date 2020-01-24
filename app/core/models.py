from django.db import models


class Deal(models.Model):
  customer_name = models.CharField(max_length=255)
  item = models.CharField(max_length=255)
  total = models.IntegerField()
  quantity = models.IntegerField()
  date = models.DateTimeField()

  def __str__(self):
    return self.customer_name
