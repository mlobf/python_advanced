
fruits = {

    'pineapple': 10,
    'watermelon': 50,
    'apple': 40,
    'grapes': 15,
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

print(p)
