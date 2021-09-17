"""
    Add a counter at a iterable and return the this
    counter .
"""
# teste
fruits = ["apple", "pineapple", "lemon", "watermelon", "grapes"]

enumerate_list = enumerate(fruits)


for index, element in enumerate_list:
    filename = f"file{index}.jpg"
    print(filename)
    
