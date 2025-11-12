import math
print("BEM VINDO A LOJA TINTASLARAS")
metroQuadrado = float(input('Digite o tamanho em metros quadrados a área a ser pintada: '))

litrosNecessarios = metroQuadrado / 6

litros_margem = (litrosNecessarios * 0.10) + litrosNecessarios

latas = math.ceil(litros_margem / 18)
precoTotalLata = latas * 80

galoes = math.ceil(litros_margem / 3.6)
precoTotalGalao = galoes * 25

qntds_latas = math.floor(litros_margem / 18)
sobraLitros = math.ceil(litros_margem % 18)

qntds_galoes = math.ceil(sobraLitros / 3.6)

preco_latas = qntds_latas * 80
preco_galoes = qntds_galoes * 25

precoTotal = preco_latas + preco_galoes

print(f'A quantidade total de latas a serem utilizadas é de {latas} e o preço total delas é de R${precoTotalLata:.2f}')
print(f'A quantidade total de galões a serem utilizados é de {galoes} e o preço total delas é de R${precoTotalGalao:.2f}')
print(f'A quantidade total de latas e galões a serem utilizados é de {qntds_latas} latas por R${preco_latas:.2f} e {qntds_galoes} galões por R${preco_galoes:.2f} e o preço total delas é de R${precoTotal:.2f}')
