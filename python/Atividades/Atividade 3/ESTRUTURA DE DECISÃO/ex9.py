numeros = []

for i in range(3):
    n = float(input(f'Digite o {i+1}° número: '))
    numeros.append(n)

if numeros[0] < numeros[1]:
    numeros[0], numeros[1] = numeros[1], numeros[0]

if numeros[0] < numeros[2]:
    numeros[0], numeros[2] = numeros[2], numeros[0]

if numeros[1] < numeros[2]:
    numeros[1], numeros[2] = numeros[2], numeros[1]

print("Números em ordem decrescente:", numeros)
