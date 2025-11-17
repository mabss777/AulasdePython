perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?','Já trabalhou com a vítima?']

negativas = 0
positivas = 0

for i in range(5):
    resposta = input(f'{perguntas[i]} Responda Sim ou Não: ')
    if resposta == "Sim":
        positivas += 1
    elif resposta == 'Não':
        negativas += 1
if positivas == 2:
    print('Você foi classificado como suspeito.')

elif (positivas == 3) and (positivas == 4):
    print('Você foi classificado como cúmplice.')
        
elif positivas == 5:
    print('Você foi considerado como assasino.')
        
else:
    print('Você foi considerado como inocente.')
