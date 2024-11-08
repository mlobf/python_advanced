import sys
import time

beg = time.time()


def square(x):
    result = x * 2


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = range(100000000)

# tuple(map(square, lista))  # ok

# list(map(square, lista))  # 6.9186217785
# print(type(list(map(square, lista))))
# Retorna uma lista

# tuple(map(square, lista))  # 6.9476320744
# print(type(tuple(map(square, lista))))
# Retona uma tupla

# map(square, lista)  # 1.9458e-06
# print(sys.getsizeof(map(square, lista)))  # Size de 48 Bytes
# retorna um map

# print(type(map(square, lista)))  # 1.9058e-06
# retorna um map

# 9.964785099
"""
for l in lista:
    square(l)

"""

# [square(_) for _ in lista]  # 8.9443943501
# print(type([square(_) for _ in lista]))  # retorna uma lista

# Agora o Canhao do Generator
# (square(_) for _ in lista)  # 2.3842e-06
# list(g)) Deu para converter em lista

# print(sys.getsizeof([square(l) for l in lista if l > 10]))  # Size 835128600 bytes
# print(sys.getsizeof([square(_) for _ in lista if _ > 10]))  # Size 835128600 bytes Nao Mudou de tamanho

# Agora usando uma lambda
print(sys.getsizeof(map(lambda i: i**2, lista)))  # Size de 48 bytes


end = time.time()

print(round(end - beg, 10))
