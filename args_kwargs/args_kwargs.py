# *args is a tuple
def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6))

# **kwargs is a dict


def print_fruits(**kwargs):

    """
    The importance of **kwargs
    There is a famous book every software developer should read: Clean Code: A Handbook of Agile Software Craftsmanship
    In this book, it is stated that functions ideally should have 0 arguments.
    If it has 1 argument, that's OK.
    If it has 2 arguments, that's acceptable.
    If it has 3 arguments, you should check if you could make it 2, but it is still acceptable.
    But if it has more than 3 arguments, that function is bad written.
    Sometimes it is impossible to write a function without arguments, but it's always
        possible to use **kwargs to specify other arguments. That's what lots of libraries
        like matplotlib do. For example, look at the docs of this function: plot
    It uses **kwargs to specify parameters like the color, the linewidth, etc.
        Then you can use what we are going to learn about the .get() method
        from dictionaries to see if a specific key is present in **kwargs or not.
    """

    for key, value in kwargs.items():
        print(key, value)


print_fruits(apple=60, watermellon=100, grapes=200)
