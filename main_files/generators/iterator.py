fruits = ["apple", "watermellon", "grapes"]

fruits = iter(fruits)
# fruits.__next__()
"""
print(next(fruits))
print(next(fruits))
print(next(fruits))
"""

# This is eq as
y = iter(range(1, 11))

for i in y:
    print(i)

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done")
        break
