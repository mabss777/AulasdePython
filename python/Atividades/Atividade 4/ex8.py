numeros = []

for i in range(3):
   n = float(input(f'Qual o preço do {i+1}° produto: '))
   numeros.append(n)

if (numeros[0] < numeros[1]) and (numeros[0] < numeros[2]):
    print(f'O produto que você deve comprar é o {numeros[0]} pois seu preço é o menor!')

elif (numeros[1] < numeros[0]) and (numeros[1] < numeros[2]):
    print(f'O produto que você deve comprar é o {numeros[1]} pois seu preço é o menor!')
    
else:
    print(f'O produto que você deve comprar é o de {numeros[2]} pois seu preço é o menor!')
