def wrapper(f):
    def inner():
        print("Im a decorated function!!!")
        f()

    return inner


@wrapper
def hello_world():
    print("hello world")


hello_world()
