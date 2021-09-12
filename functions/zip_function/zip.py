

"""
-The zip functions takes some iterators and
zips Them on Tuples.
- Used to parallel iterations
- Retuns a zip object which is an iterators of tuples.
"""

countries = ["Ecuador", "Peru", "Colombia", "USA", "Brazil"]
capitals = ["Quito", "Lima", "Bogota", "Washintown DC", "Brasila"]


countries_capitals = zip(countries, capitals)

print(countries_capitals.__next__())
print('-------')
print(countries_capitals.__next__())
