import random

notas = []

for i in range(20):
    n = int(input(f'Digite a {i+1}° nota: '))
    notas.append(n)




    if n == -1:
        print('Entrada de dados encerrada!')

        valores = 0
        for i in range(20):
            if (notas[i] >= 0) and (notas[i] <= 10):
                valores += 1
        
        

        print(f'A quantidade de números lidos foi de {valores} \nEsses foram os valores: {notas} \n')
