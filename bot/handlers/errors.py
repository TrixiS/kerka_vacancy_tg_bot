import logging

from ..bot import DISPATCHER


@DISPATCHER.errors_handler()
async def errors_handler(exception: Exception):
    logging.exception(exception, exc_info=True)
