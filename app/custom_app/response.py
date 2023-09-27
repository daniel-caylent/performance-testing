"""Module that defines a standard response for all lambdas that serve the API Gateway"""

import json

from dataclass.encoder import encode


def response(code: int, id_: str, **kwargs):
    """Generate json encodable and consistent responses for lambda functions"""
    response_ = {
        "statusCode": code,
        "isBase64Encoded": False,
        "headers": {
            "x-aws-lambda-id": id_,
        }
    }

    data = encode(kwargs.pop("data", None))
    if len(kwargs) > 0:
        body = {}
        for key, value in kwargs.items():
            body[key] = encode(value)
        if data:
            body["data"] = data

    elif data:
        body = data

    response_["body"] = json.dumps(body)
    return response_
