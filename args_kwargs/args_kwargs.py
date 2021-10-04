

# *args is a tuple
def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6))


# **kwargs is a dict
def print_fruits(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print_fruits(apple=60, watermellon=100, grapes=200)
