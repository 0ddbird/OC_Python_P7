import time
from functools import wraps


def perf_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"{func.__name__} execution time: {end_time - start_time} seconds"
        )
        return result

    return wrapper
