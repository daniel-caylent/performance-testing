import json
import uuid

from endpoint import endpoint
import models
from dataclass.error import dataclass_error_to_str

def __get_data(search):
    """Generate static data"""
    return [
        models.Data(name=f"{search}-{i}", number=i)
        for i in range(1000)
    ]


@endpoint
def get_data(event):
  params = event.get("queryStringParameters") or {}
  try:
      search = models.Search(**params)
  except Exception as e:
      return 400, {"detail": dataclass_error_to_str(e)}

  data = __get_data(search.search)
  return 200, {"data": data}

@endpoint
def post_data(event):
    if not event.get("body"):
        return 400, {"detail": "No body detected."}

    try:
        json_parsed = json.loads(event["body"])
    except:
        return 400, {"detail": "Unable to parse JSON from body."}

    try:
        post = models.Post(**json_parsed)
    except Exception as e:
        return 400, {"detail": dataclass_error_to_str(e)}

    # create record here... outside the scope!
    record_id = str(uuid.uuid4())
    return 201, {"id": record_id}
