import numpy

idades = [32, 14, 47, 28, 19, 55, 23, 41, 12, 36,27, 53, 15, 49, 33, 22, 45, 10, 38, 26,34, 18, 52, 29, 44, 13, 25, 40, 31, 21]

alturas = [1.72, 1.58, 1.90, 1.63, 1.55, 1.84, 1.69, 1.47, 1.78, 1.60,1.82, 1.52, 1.66, 1.74, 1.57, 1.93, 1.49, 1.70, 1.88, 1.61,1.68, 1.50, 1.81, 1.56, 1.76, 1.53, 1.85, 1.64, 1.71, 1.59]

media_alturas = numpy.mean(alturas)

alunos = 0
for i in range(30):
    if (idades[i] > 13) and (alturas[i] < media_alturas):
     if i >= 13:
        alunos += 1

print(f'Possuem {alunos} alunos com mais de 13 anos com a altura inferior à média das alturas')




