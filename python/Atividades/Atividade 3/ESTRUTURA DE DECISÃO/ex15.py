a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados formam um triângulo!")

    if a == b == c:
        print("Tipo: Equilátero")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")
else:
    print("Os lados NÃO formam um triângulo.")
