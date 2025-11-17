idades = []
alturas = []

for i in range(5):
    idades.append(int(input("Idade: ")))
    alturas.append(float(input("Altura: ")))

print("Idades invertidas:", idades[::-1])
print("Alturas invertidas:", alturas[::-1])
