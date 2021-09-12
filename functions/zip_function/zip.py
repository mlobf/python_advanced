"""
-The zip functions takes some iterators and
zips Them on Tuples.
- Used to parallel iterations
- Retuns a zip object which is an iterators of tuples.

the zip function takes the len of the shortest list
    ands used it as main path to zip to the other list.
"""

countries = ["Ecuador", "Peru", "Colombia", "USA", "Brazil", "Chile"]
capitals = ["Quito", "Lima", "Bogota", "Washintown DC", "Brasila"]


countries_capitals = zip(countries, capitals)

print(type(countries_capitals))

for countries, capitals in countries_capitals:

    print(countries, capitals)


print(type(list(countries_capitals)))
