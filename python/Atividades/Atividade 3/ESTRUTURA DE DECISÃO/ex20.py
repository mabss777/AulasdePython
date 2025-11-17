import numpy
import math 

notas = []

for i in range(3):
    n = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(n)

media = numpy.mean(notas)

if media == 10:
    print(f'Parabéns! Você foi aprovado com distinção, sua média foi {media:.2f}')

elif media >= 7:
    print(f'Parabéns! Você foi aprovado, sua média foi {media:.2f}')

else:
    print(f'Você foi reprovado, sua média foi {media:.2f}')
