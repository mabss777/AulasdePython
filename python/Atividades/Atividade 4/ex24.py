n1 = float(input("1º número: "))
n2 = float(input("2º número: "))
op = input("Operação (+, -, *, /): ")

if op == '+':
    r = n1 + n2
elif op == '-':
    r = n1 - n2
elif op == '*':
    r = n1 * n2
elif op == '/':
    r = n1 / n2
else:
    print("Opção inválida.")
    exit()

