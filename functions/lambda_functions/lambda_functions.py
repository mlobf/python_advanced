"""
    Lambda Functions are important for functional programming
        They are unamed, annonimous functions

    syntax 
        lambda arg: expression

add = lambda x: x + 5

print(add(10))
"""

lambda_functions = [lambda x: x+j for j in range(3)]

first_lambda_function = lambda_functions[0]



print(first_lambda_function(5))