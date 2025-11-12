kgPeixe = int(input('Digite quantos KG de peixe você tem: '))

maxPeixe = 50
peixesaMais= kgPeixe - maxPeixe
totalPagar = peixesaMais * 4
if kgPeixe > maxPeixe:
    print(f'A quantidade de {kgPeixe}KG de peixe excedeu o limite! Você terá que pagar: R${totalPagar}')
else:
    print(f'A quantidade de {kgPeixe}KG está dentro do limite! Não será preciso pagar a multa!')
