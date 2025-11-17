A = []
for i in range(10):
    A.append(int(input("Número: ")))

soma = 0
for n in A:
    soma += n*n

print("Soma dos quadrados:", soma)
