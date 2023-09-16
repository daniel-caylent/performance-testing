"""Module that defines a decorator for all lambdas that serve the API Gateway"""

from functools import wraps
import sys
import traceback

from response import response
from logger import use_logging


def endpoint(func):
    """
    Decorator used to enable logging and error catch/response for lambda APIs
    """

    @wraps(func)
    def wrapper(event, context):
        func_with_logging = use_logging(func)
        try:
            code, data = func_with_logging(event, context)
            return response(code, context.aws_request_id, **data)

        except Exception as e:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            traceback_string = traceback.format_exception(
                exception_type, exception_value, exception_traceback
            )
            return response(
                500, context.aws_request_id, detail=f"Internal Server Error: {traceback_string}"
            )

    return wrapper
