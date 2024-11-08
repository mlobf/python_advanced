"""
-The zip functions takes some iterators and
zips Them on Tuples.
- Used to parallel iterations
- Retuns a zip object which is an iterators of tuples.

the zip function takes the len of the shortest  tuples
    ands used it as main path to zip to the other tuples.
"""


countries = ("Ecuador", "Peru", "Colombia", "USA", "Brazil", "Chile")

capitals = ("Quito", "Lima", "Bogota", "Washintown DC", "Brasila", "Santiago")

countries_capitals = zip(countries, capitals)

print(list(countries_capitals))
