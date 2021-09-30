import pdb


fruits = {
    "pineapple": 10,
    "watermelon": 50,
    "apple": 40,
    "grapes": 15,
}


def get_quantity(fruit):
    """
    Get the value
    """
    return fruits[fruit]


# print(fruits['apple'])


# Sorting as get values instead key

# p = sorted(fruits, key=get_quantity)

p = sorted(fruits, key=lambda fruit: fruits[fruit])

# print(p)


mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]

print({i: mylist.index(i) for i in list_b})
