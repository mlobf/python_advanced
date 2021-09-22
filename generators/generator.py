import sys

"""
ITERATOR ->  An object that enables a programmer to
            traverse a conteiner, particulary lists.
"""

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("==================>", sys.getsizeof(x))


for element in x:
    print(element)


y = range(1, 11)
for i in y:
    print(i)


print("=================>", sys.getsizeof(y))
