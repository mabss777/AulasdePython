import numpy
import math 

notas = []

for i in range(4):
    n = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(n)

media = numpy.mean(notas)

print(f'Suas notas foram: {notas} \nE sua média é {media:.2f}!')
