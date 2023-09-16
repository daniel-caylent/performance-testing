"""Standard logging module"""

from functools import wraps
import logging
import json
import os
import sys
import traceback

LOG_LEVEL = os.environ.get("LOG_LEVEL", "ERROR").upper()
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)


def use_logging(func):
    """
    Wrapper to run a function with good logging for lambda functions
    """

    @wraps(func)
    def wrapper(event, context):
        logger.info("event: %s", event)
        logger.info("context: %s", context)

        try:
            result = func(event)
            return result

        except Exception as e:
            exception_type, exception_value, exception_traceback = sys.exc_info()
            traceback_string = traceback.format_exception(
                exception_type, exception_value, exception_traceback
            )
            err_msg = json.dumps(
                {
                    "errorType": exception_type.__name__,
                    "errorMessage": str(exception_value),
                    "stackTrace": traceback_string,
                }
            )
            logger.error("event: %s", event)
            logger.error("context: %s", context)
            logger.error(err_msg)
            raise e

    return wrapper
