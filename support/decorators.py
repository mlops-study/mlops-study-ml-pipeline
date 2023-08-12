import time
import functools


def elapsed_time(func):
    """This is a decorator which can be used to print elapsed time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        _elapsed_time = int(time.time() - start_time)
        print(f"elapsed_time = {_elapsed_time} sec")
        return result
    return wrapper
