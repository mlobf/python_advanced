"""
    Algoritimo de Sort
    Tenho que ordenar os alunos de uma sala.
        metade esta de uniforme preto,
        metade esta de uniforme laranja,

    Uma fila preenchida com alunos com uniformes de uma so cor.
    O aluno da primeira fila tem que ser mais baixo que o aluno da segunda fila.
"""

alunos_preto = [150, 179, 149, 152, 154]
alunos_laranja = [162, 181, 151, 160, 170]

nap = sorted(alunos_preto)
nal = sorted(alunos_laranja)


new_alunos = zip(nap, nal)

new_lista = []
for x in list(new_alunos):
    r = x[1] - x[0]
    new_lista.append(r)


for x in new_lista:
    if x <= 0:
        print("deu ruim")
