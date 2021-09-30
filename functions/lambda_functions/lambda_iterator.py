"""
print(lambda x: x for x in range(10))
"""

# print((lambda x, y: x * y)(int(5), int(7)))

# print((lambda x, y=3, z=5: x*y*z)(7))

# lambda arguments: expression

lambda_functions = [lambda x: x + j for j in range(3)]

first_lambda_function = lambda_functions[0]
print(first_lambda_function)
