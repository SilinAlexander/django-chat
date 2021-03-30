import logging

from requests.exceptions import RequestException
from kombu.exceptions import OperationalError
from timeit import default_timer

logger = logging.getLogger(__name__)


def execution_time(func) -> object:
    def delta_time(*args, **kwargs):
        t1 = default_timer()
        data = func(*args, **kwargs)
        delta = default_timer() - t1
        logger.info(f'Function: {func.__name__}, Run time: {delta}')
        logger.info(f'Returned data: {data}, Type: {type(data)}')
        logger.info('############ SEPARATING ############')
        return data
    return delta_time


def except_shell(errors=(Exception,), default_value=''):
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                logging.error(e)
                return default_value or None
        return new_func
    return decorator


request_shell = except_shell((RequestException,))
celery_shell = except_shell((OperationalError,))