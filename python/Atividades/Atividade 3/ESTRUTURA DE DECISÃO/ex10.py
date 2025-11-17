turno = input('Em qual turno você estuda? \nM - Matutino \nV - Vespertino \nN - Noturno \n Digite a respectiva letra: ')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido.')