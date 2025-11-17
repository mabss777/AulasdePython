numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'{numero} é um número par!')

elif numero % 2 != 0:
    print(f'{numero} é um número ímpar!')

else:
    print('Número inválido')