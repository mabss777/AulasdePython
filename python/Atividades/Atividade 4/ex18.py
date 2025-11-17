dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

valida = False

if mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia <= 31:
        valida = True

elif mes in [4, 6, 9, 11]:
    if dia <= 30:
        valida = True

elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia <= 29:
            valida = True
    else:
        if dia <= 28:
            valida = True

# AGORA sim o print está fora do if do mês
if valida:
    print(f'{dia}/{mes}/{ano} é uma data válida!')
else:
    print('Data inválida.')
