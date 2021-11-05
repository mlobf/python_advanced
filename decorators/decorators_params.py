import time


def time_to_run(f):
    def inner(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"This function took {execution_time}")

    return inner


@time_to_run
def hello_world():
    for _ in range(100):
        print("hello world")


hello_world()
