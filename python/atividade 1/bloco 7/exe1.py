ano_nasc = (int(input('Digite o ano em que você nasceu: ')))
idade = 2025 - ano_nasc

if idade > 65:
    print('Você já pode se aposentar! :)')
else:
    print('Ainda não chegou seu momento de aposentar... :(')