tipo = input("Tipo (F=File, A=Alcatra, P=Picanha): ").strip().upper()
kg = float(input("Quantidade (kg): "))

if tipo == "F":
    preco = 4.90 if kg <= 5 else 5.80

elif tipo == "A":
    preco = 5.90 if kg <= 5 else 6.90

elif tipo == "P":
    preco = 6.80 if kg <= 5 else 7.80

else:
    print("Tipo inválido."); exit()

total = kg * preco

pag_cartao = input("Pagamento com cartão Tabajara? (S/N): ").strip().upper() == "S"

desconto = total * 0.05 if pag_cartao else 0.0

a_pagar = total - desconto

print("=== CUPOM ===")
print(f"Carne: {tipo}, Kg: {kg}")
print(f"Preço total: R${total:.2f}")
print(f"Pagamento cartão: {'Sim' if pag_cartao else 'Não'}")
print(f"Desconto: R${desconto:.2f}")
print(f"Valor a pagar: R${a_pagar:.2f}")
