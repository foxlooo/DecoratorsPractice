import logging
from functools import partial, wraps

def create_logger(log_name, file_name):
    '''
    :param log_name: String
    :param file_name: String
    :return: Logger
    '''
    log = logging.getLogger(log_name)
    log.setLevel(logging.DEBUG)

    if not log.handlers:
        fh = logging.FileHandler(file_name, 'a+')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        log.addHandler(fh)

    return log

def log_decorator(file_name):
    '''
    :param file_name: String: The filename that you would like the logging to go to
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = create_logger(func.__name__, file_name)
            try:
                logger.debug(f"Running {func.__name__}")
                return func(*args, **kwargs)
            except:
                logger.exception(f"Error running {func.__name__}")
                raise
        return wrapper
    return decorator

