from itertools import zip_longest


"""
    This one takes the longest iterable - list, tuple, dict, etc
    instead of the shortest
"""

countries = ("Ecuador", "Peru", "Colombia",
             "USA", "Brazil", "Chile", "Bolivia")

capitals = ("Quito", "Lima", "Bogota", "Washintown DC", "Brasila", "Santiago")

countries_capitals = zip_longest(
    countries, capitals, fillvalue="My Default City")

print("------------------")

print(type(countries_capitals))

print("------------------")
print(list(countries_capitals))

print("------------------")
print(type(list(countries_capitals)))
