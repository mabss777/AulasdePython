litros = float(input("Litros: "))
tipo = input("Tipo (A/G): ").strip().upper()
preco = 1.90 if tipo == "A" else 2.50

if tipo == "A":
    desconto = 0.03 if litros <= 20 else 0.05

else:
    desconto = 0.04 if litros <= 20 else 0.06

total = litros * preco
pag = total * (1 - desconto)
print(f"Total: R${pag:.2f}")
