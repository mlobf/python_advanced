"""
    Recebe um array nao vazio que possui inteiros distintos e um
    inteiro respersentando uma soma alvo.
    Caso dois numeros no array de entrada gerar a soma alvo,
    ele devem retornar estes dois numeros no array de saida.
    Se nao gera retorna vazio.
"""


"""
    Parametro 1 => Array de inteiros
    Parametro 2 => Valor alvo que é a soma de dois numeros.
"""
myarray = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10


def my_func(myarray, target):
    soma = 0
    v1 = 0
    v2 = 0
    p1 = 0
    p2 = p1 +1

    resultado = {"p1": p1, "v1": v1, "p2": p2, "v2": v1, "soma": soma}
    # Metodo Força Bruta
    while p1 is not len(myarray) - 1:
        while p2 is not len(myarray):
            v1 = myarray[p1]
            v2 = myarray[p2]
            soma = v1 + v2
            p2 += 1
            if soma == target:
                resultado["p1"] = p1
                resultado["v1"] = v1
                resultado["p2"] = p2
                resultado["v2"] = v2
                resultado["soma"] = soma
                break
        p2 = 1
        p1 += 1

    return resultado


print(my_func(myarray, target))
