"""
    Applies a given function to each item of an iterable.
    The map fuctions returns a map object which is an iterable.
    Use instead of loops wherever you can.
"""

# Capitalize all Strings of a list.

# Old way
fruits = ['apple', 'watermellon', 'pineapple', 'grapes']
new_fruits = []

# for f in fruits:
#    new_fruits.append(f.upper())

# print(new_fruits)

result = map(lambda fruit: fruit.upper(), fruits)


print(list(result))
