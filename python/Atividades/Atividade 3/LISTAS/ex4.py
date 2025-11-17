chars = []

for i in range(10):
    letra = input(f"Digite a {i+1}ª letra: ").strip()
    chars.append(letra)

vogais = "aeiouAEIOU"
consoantes = []

for c in chars:
    if c.isalpha() and c not in vogais:
        consoantes.append(c)

print("Quantidade:", len(consoantes))
print("Consoantes:", consoantes)
