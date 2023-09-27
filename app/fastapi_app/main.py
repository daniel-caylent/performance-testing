import uuid
import os

from fastapi import FastAPI, Request, Response, Depends
from mangum import Mangum

import models

app = FastAPI(
  root_path="/v1"
)

def __get_data(search):
    """Generate static data"""
    return [
        models.Data(name=f"{str(search)}-{i}", number=i)
        for i in range(1000)
    ]

@app.get("/fastapi")
def get_data(search: models.Search = Depends()):

  data = __get_data(search.search)
  return data

@app.post("/fastapi")
def post_data(post: models.Post, response: Response):

    # create record here... outside the scope!
    record_id = uuid.uuid4()

    response.status_code = 201
    return {"id": record_id}

@app.middleware("http")
async def add_event_id(request: Request, call_next):
    response = await call_next(request)
    request_id = request.scope["aws.context"].aws_request_id
    response.headers["x-aws-lambda-id"] = request_id
    return response


handler = Mangum(app)
