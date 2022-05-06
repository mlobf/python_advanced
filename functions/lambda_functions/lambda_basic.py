# l = lambda x:x
# def l(x): return x

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
print((lambda x: x + 5)(5))
print((lambda x: x - 5)(5))
print((lambda x: x * 5)(5))
print((lambda x: x**5)(5))
"""
new_list = []

[new_list.append(x + 1) for x in lista if x % 1 == 0 and x % 5 == 0]

print(new_list)

# print(add(4))
# print(less(4))
# print(mult(4))
# print(pot(4))
