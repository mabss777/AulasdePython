import math 

nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print('PARABÉNS! VOCÊ FOI APROVADO. Sua média foi', media)
elif media < 7:
    print('REPROVADO... sua média foi', media)
else:
    print('APROVADO COM DISTINÇÃO! sua média foi', media)