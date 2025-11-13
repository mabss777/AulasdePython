n1 = 'Olá gente'
print(n1)
print(f'O tipo primitivo desse valor é {(type(n1))}')
print('É um número?', n1.isnumeric())
print('É alfabético?', n1.isalpha())
print('Está em maiúscula?', n1.isupper())
print('Está capitalizada?', n1.capitalize())
print('Quantas letras A tem?', n1.count('e')) 
print(n1.swapcase())
