"""
-The zip functions takes some iterators and
zips Them on Tuples.
- Used to parallel iterations
- Retuns a zip object which is an iterators of tuples.

the zip function takes the len of the shortest dict
    ands used it as main path to zip to the other dict.
"""

products = {"apple": 1.0, "pineapple": 1.4}

tech = {"iphone": 1.000000, "motorola": 1.000000}

products_tech = zip(products.values(), tech.values())

print(list(products_tech))
