numeros = []
for i in range(5):
    numeros.append(int(input("Número: ")))

soma = sum(numeros)

produto = 1
for n in numeros:
    produto *= n

print("Números:", numeros)
print("Soma:", soma)
print("Multiplicação:", produto)
