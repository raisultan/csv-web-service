from dateutil import parser


def check_deal_validity(dealinfo):
  if (
    isinstance(dealinfo[0], str)
    and isinstance(dealinfo[1], str)
    and dealinfo[2].isdigit()
    and dealinfo[3].isdigit()
  ):
    try:
      parser.parse(dealinfo[4])
    except:
      return False
    else:
      return True

  else:
    return False


def check_item_existence_for_client(client, item):
  try:
    client.gems.get(name=item)
  except:
    return False
  else:
    return True


def create_most_valuable_clients_list(model, attr):
  if len(model.objects.all()) >= 5:
    clients = model.objects.order_by(attr)[:5]
  else:
    clients = model.objects.order_by(attr)

  for client in clients:
    gems_filter_set = set()
    for gem in client.gems.all():
      for other_client in clients:
        if client is not other_client:
          if len(gem.clients.filter(username=other_client.username)) > 0:
            gems_filter_set.add(gem)

    client.gems.filter(name__in=gems_filter_set)

  return clients
