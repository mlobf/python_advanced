"""
    Why use generators ?

    
        Because there easier to implement then iterators.
        Memory efficient.
        Excellent to generate inifinit streams.
        They can be pipelined.

"""


numbers = [3, 6, 9]
powers = (x ** 2 for x in numbers)


# print(next(powers))
# print(next(powers))
# print(next(powers))

for n in numbers:
    try:
        print(next(powers))
    except Exception:
        pass
