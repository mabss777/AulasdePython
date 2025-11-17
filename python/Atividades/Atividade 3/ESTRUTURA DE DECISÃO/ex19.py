numero = int(input('Digite um número menor que 1000: '))

if (numero >= 100) and (numero <= 1000):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    
    print(f'{numero} = {centenas} centena(s), {dezenas} dezena(s) e {unidades} unidade(s).')

elif (numero >= 10) and (numero <= 99):
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    
    print(f'{numero} = {dezenas} dezena(s) e {unidades} unidade(s).')

elif (numero >= 0) and (numero <= 19):
    unidades = numero % 10
    
    print(f'{numero} = {unidades} unidade(s).')

else:
    print('Isso não é um número!')
