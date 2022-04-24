import time
import sys

lista = range(10000000000000)


def time_to_run(f):
    def inner(*args, **kwargs):
        start = time.time()

        f(*args, **kwargs)

        end = time.time()
        execution_time = round(end - start, 10)

        print(f"This function took {execution_time}")

    return inner


def just_print(f):
    def inner(*args, **kwargs):

        f(*args, **kwargs)

        print(f"This func is a simple print")

    return inner


@just_print
@time_to_run
def testing_func():

    print(sys.getsizeof(map(lambda i: i**2, lista)))  # Size de 48 bytes


testing_func()
