numeros = []

for i in range(3):
   n = float(input(f'Digite o {i+1}° número: '))
   numeros.append(n)

print(f'O maior número digitado foi {max(numeros)} e o menor foi {min(numeros)}')