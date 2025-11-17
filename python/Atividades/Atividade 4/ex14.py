import numpy

notas = []

for i in range(2):
    n = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(n)

media = numpy.mean(notas)

if (media > 9.0) and (media < 10.0):
    print(f'Suas notas foram: {notas[0]} e {notas[1]}; \nSua média foi {media} \nSeu conceito foi A; \nVocê foi APROVADO!')

elif (media > 7.5) and (media < 9.0):
    print(f'Suas notas foram: {notas[0]} e {notas[1]}; \nSua média foi {media} \nSeu conceito foi B; \nVocê foi APROVADO!')

elif(media > 6.0) and (media < 7.5):
    print(f'Suas notas foram: {notas[0]} e {notas[1]}; \nSua média foi {media} \nSeu conceito foi C; \nVocê foi APROVADO!')

elif (media > 4.0) and (media < 6.0):
    print(f'Suas notas foram: {notas[0]} e {notas[1]}; \nSua média foi {media} \nSeu conceito foi D; \nVocê foi REPROVADO...')

elif(media < 4.0) and (media == 0.0):
    print(f'Suas notas foram: {notas[0]} e {notas[1]}; \nSua média foi {media} \nSeu conceito foi E; \nVocê foi REPROVADO...')

else:
    print('Valor inválido!')