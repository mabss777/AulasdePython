valor = int(input("Digite o valor do saque (entre 10 e 600): "))

if valor < 10 or valor > 600:
    print("Valor inválido.")
else:
    n100 = valor // 100
    resto = valor % 100

    n50 = resto // 50
    resto = resto % 50

    n10 = resto // 10
    resto = resto % 10

    n5 = resto // 5
    resto = resto % 5

    n1 = resto

    print(f"Notas fornecidas:")
    print(f"{n100} nota(s) de 100")
    print(f"{n50} nota(s) de 50")
    print(f"{n10} nota(s) de 10")
    print(f"{n5} nota(s) de 5")
    print(f"{n1} nota(s) de 1")
