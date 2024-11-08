mylist = [1, 2, 3, 4, 5, 6]
mytuple = (1, 2, 3, 4, 5, 6)
myDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

""" 
def soma_lista(*args):
    return sum(args)
"""


def soma_lista(*args):
    return sum(args)


def soma_dict(**kwargs):
    return sum(kwargs.values())


if __name__ == "__main__":
    print(soma_lista(*mytuple))
    print(soma_lista(*mylist))
    print(soma_dict(**myDict))
