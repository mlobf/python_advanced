"""
    Try to apply a more  advanced use of
    map
"""
fruits = ['apple', 'watermellon', 'pineapple', 'grapes']


def process(fruit):
    resulting_string = fruit.capitalize()
    if fruit.endswith('s'):
        resulting_string += " are great"
    else:
        resulting_string += " is great"
    return resulting_string

result = map(process, fruits)

print(list(result))
