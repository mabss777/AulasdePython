numeros = []

for i in range(3):
   n = float(input(f'Digite o {i+1}° número: '))
   numeros.append(n)

if (numeros[0] > numeros[1]) and (numeros[0] > numeros[2]):
   print('O maior número digitado foi', numeros[0])

elif (numeros[1] > numeros[0]) and (numeros[1] > numeros[2]):
   print('O maior número digitado foi', numeros[1])
   
else:
   print('O maior número digitado foi', numeros[2])
