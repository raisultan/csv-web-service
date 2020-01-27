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
