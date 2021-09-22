"""
    Do lambda function with
    a external paramet

    Do not forget to put params in the end of the lambda 
    function.
"""

x = 5

# print(lambda x: x + 1)
# print(x)

#l = (lambda x: x + 1)(5)

# print(l)

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_compras = []
contador = 0

for _ in items:
    lista_compras.append(contador)
    contador += 1

print(lista_compras)
