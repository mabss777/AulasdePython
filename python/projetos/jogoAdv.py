import random

numeroCerto = random.randint(1, 50)
contador = 0
continuar = True

print('Bem-vindo/a ao Jogo da Adivinhação!')
while continuar == True:
    print('Tente adivinhar o número de 1 a 50.')
    tentativa = (float(input('Seu palpite: ')))
    contador = contador + 1

    if tentativa > numeroCerto:
        print('Muito alto! Tente um número menor!')
    elif tentativa < numeroCerto:
        print('Muito baixo! Tente um número maior!')
    else:
        tentativa == numeroCerto
        print(f"Parabéns! Você acertou em {contador} tentativas!")
        opcao = (float(input('Quer continuar: 1 - Sim ou 2 - Não  : ')))
        if opcao == 1:
            contador == 0
            numeroCerto = random.randint(1, 50)
        else:
            print('Jogo encerrado! Obrigada por jogar!')
            break

        
        