kg_morango = float(input("Kg de morango: "))
kg_maca = float(input("Kg de maçã: "))

preco_morango = 2.50 if kg_morango <= 5 else 2.20
preco_maca = 1.80 if kg_maca <= 5 else 1.50

total = kg_morango*preco_morango + kg_maca*preco_maca

if (kg_morango+kg_maca) > 8 or total > 25:
    total *= 0.90

print(f"Valor a pagar: R${total:.2f}")
