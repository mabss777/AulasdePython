import numpy

temperaturas = [24.7, 24.8, 23.9, 22.1, 19.0, 17.3, 16.5, 17.3, 18.6, 20.4, 21.8, 23.7]
meses = ['1 - Janeiro', '2 - Fevereiro','3 - Março', '4 - Abril', '5 - Maio', '6 - Junho', '7 - Julho', '8 - Agosto', '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']

media_anual = numpy.mean(temperaturas)

print(f'Média anual = {media_anual:.1f}°C')

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f'{meses[i]} com a temperatura média de {temperaturas[i]}°C')