import math

metroQuadrado = int(input('Digite o tamanho em metros quadrados a área a ser pintada: '))

litrosNecessarios = metroQuadrado / 6
latas = math.ceil(litrosNecessarios / 18)
precoTotal = latas * 80

print(f'A quantidade total de latas a serem utilizadas é de {latas} e o preço total delas é de R${precoTotal:.2f}')