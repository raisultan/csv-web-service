import csv

from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from celery.utils.log import get_task_logger
from celery import shared_task

from core.models import Item, Client, Deal
from .utils import check_deal_validity, check_item_existence_for_client

logger = get_task_logger(__name__)


@shared_task
def process_file(path):
  with open(path) as csv_file:
    reader = csv.reader(csv_file)

    logger.info("Processing file")

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

        deal = Deal(
          client=Client.objects.get(username=row[0]),
          item=Item.objects.get(name=row[1]),
          total=row[2],
          quantity=row[3],
          date=row[4],
        )
        deal.save()
        Client.objects.filter(username=deal.client) \
          .update(spent_money=F('spent_money') + deal.total)
        if check_item_existence_for_client(
          client=deal.client,
          item=deal.item
        ):
          pass
        else:
          deal.client.gems.add(deal.item)
