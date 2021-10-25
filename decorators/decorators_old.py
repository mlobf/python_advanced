"""
    to pass functions as arguments to other functions.
    Aka -> filter or map
    Higher order functions, and this functions can return other
        functions also.
    



"""
# First define outside function.
#
def wrapper(f):
    def inner():
        print("Im a decorated function!!!")
        f()

    return inner


def hello_world():
    print("hello world")


decorated_hello_word = wrapper(hello_world)

decorated_hello_word()
