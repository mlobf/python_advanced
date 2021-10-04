"""
    The filter function.

        Is a filter to a iterable based in a condition
            given by a function.
"""

fruits = ['apple', 'avocado', 'watermellon', 'grapes']

filtred_fruits = filter(lambda fruit: fruit.startswith("a") == True, fruits)

# new_filtered = list(filtred_fruits)

# print(type(filtred_fruits))

print(list(filtred_fruits))



