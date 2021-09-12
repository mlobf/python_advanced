"""
-The zip functions takes some iterators and
zips Them on Tuples.
- Used to parallel iterations
- Retuns a zip object which is an iterators of zip.

the zip function takes the len of the shortest  zip
    ands used it as main path to zip to the other zip.
"""


countries = "Ecuador"

capitals = "Quito"

countries_capitals = zip(countries, capitals)

print(list(countries_capitals))
