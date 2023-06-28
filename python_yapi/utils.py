import logging
import time


def log(func=None, *, verbosity=1):
    """
    Decorator for logging
    :param func:
    :param verbosity: verbosity level(default as 1)
    :return: decorator or function
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if verbosity > 0:
                func_merged_args = list([str(arg) for arg in args]) + [f'{key}={value}' for key, value in
                                                                       kwargs.items()]  # todo handle logging password
                logging.info(f"Call {func.__name__} args: {', '.join(func_merged_args)}")

            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = round(time.time() - start_time, 2)
            if verbosity > 1:
                logging.info(f"Call {func.__name__} elapsed time: {elapsed}s result: {result}")
            return result

        return wrapper

    return decorator if func is None else decorator(func)
