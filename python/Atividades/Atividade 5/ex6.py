import numpy
import math

medias = []

for a in range(10):
    print(f'\nAluno {a+1}:')
    
    notas = []
    for i in range(4):
        n = float(input(f'Digite a {i+1}ª nota: '))
        notas.append(n)

    media = numpy.mean(notas)
    medias.append(media)

    print(f'Notas: {notas}')
    print(f'Média: {media:.2f}')

aprovados = 0
for m in medias:
    if m >= 7:
        aprovados += 1

print(f'\nQuantidade de alunos com média >= 7: {aprovados}')
