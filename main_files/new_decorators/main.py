"""
Como criar um decorator personalizado
"""

from functools import wraps
from time import perf_counter, sleep


def get_time(func):
    """Time any function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time: float = perf_counter()
        func(*args, **kwargs)
        end_time: float = perf_counter()
        total_time: float = round(end_time - start_time, 3)
        print(f"The time:", total_time)

    return wrapper


@get_time
def do_something(param: str):
    """Do do_something important"""
    sleep(1)
    print(param)


if __name__ == "__main__":
    do_something("Hello !!!")
