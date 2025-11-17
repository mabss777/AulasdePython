import numpy

notas = []

for i in range(4):
    n = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(n)

print('Sua média final é:', numpy.mean(notas))
