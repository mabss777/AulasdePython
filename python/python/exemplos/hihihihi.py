n2 = int(input('Digite um valor: '))
n3 = int(input('Digite outro valor: '))
soma = n2+n3
print(type(n2))
print('A soma vale', soma)
print('A soma entre {} e {} vale {}'.format(n2, n3, soma))
print(f'A soma {n2} e {n3} vale {soma}')

n1 = input('Digite algo: ')
print(n1.isnumeric()) #aceita somente numeros
print(n1.isalpha()) #aceita somente letras
print(n1.isalnum()) #aceita letras e numeros
print(n1.isspace()) #so vai ser verdadeiro se as aspas estiverem vazias
print(n1.isupper()) #verifica se todas as letras são maiusculas
print(n1.islower()) #verifica se todas as letras são minusculas
print(n1.capitalize()) #deixa só a primeira letra em maiúscula
print(n1.startswith('a')) #verifica se inicia com a letra escolhida
print(n1.endswith('a')) #verifica se finaliza com a letra escolhida

print(n1.count('a')) #Conta quantas vezes 'a' aparece na string
print(n1.swapcase()) #Inverte maiúsculas e minúsculas
print(n1.rstrip()) #Remove espaços à direita
print(n1.strip()) #Remove espaços antes e depois do texto
print(n1.lstrip()) #Remove espaços à esquerda
