from functools import reduce


"""
    The reduce function is almost important as map function.

    His context is Big Data.

        Big Data has two main functions, map end reduce.

    The map function does the reverse of reduce function.
    The reduce function has the advantage to reduce the iterable to
        a single value. Optimazing size of it.
    Using reduce function at a list, the list will be transform
        to a single value, aka: ->
        From:
            [1,2,3,4,5,6,7]
        to:
            ((((((1+2)+3)+4)+5)+6)+7)


        the reduce function takes two arguments,
        the first is the function that will be executed for each elements
        the second is the is the sequece of the objects. 

        if in the first argument is a lambda function,
        as -> lambda x,y where the x is the current element and
        y is the result of the last iteration,
        so ->  
        reduce((lambda x,y : x*y), myList)

"""


# print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
#print(reduce(lambda x, y: x+y, range(1, 10000)))

myList = [1, 2, 200, 3, 4, 5, 90]

prod = reduce((lambda x, y: x*y), myList)

"""
    1 1 = 1
    2 1 = 2
    3 2 = 6
    4 6 = 24
    5 24 = 120

"""

print(prod)

greatest = reduce((lambda x, y: y if(y > x) else x), myList)
# Show the greatest number in myList

print(greatest)
