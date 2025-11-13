salario = float(input('Digite o valor do seu salário: '))

if salario <= 280.00:
    aumento = (salario * 0.2)
    novoSalario = salario + aumento
    print(f'Seu salário era de R${salario:.2f} \nO percentual para reajuste foi de 20%; \nO valor do aumento foi de R${aumento:.2f}; \nSeu novo salário será de R${novoSalario:.2f}!')

elif (salario >= 280) and (salario < 700):
    aumento = salario * 0.15
    novoSalario = salario + aumento
    print(f'Seu salário era de R${salario:.2f} \nO percentual para reajuste foi de 15%; \nO valor do aumento foi de R${aumento:.2f}; \nSeu novo salário será de R${novoSalario:.2f}!')

elif (salario >= 700) and (salario < 1500):
    aumento = salario * 0.1
    novoSalario = salario + aumento
    print(f'Seu salário era de R${salario:.2f} \nO percentual para reajuste foi de 10%; \nO valor do aumento foi de R${aumento:.2f}; \nSeu novo salário será de R${novoSalario:.2f}!')

elif salario > 1500:
    aumento = salario * 0.05
    novoSalario = salario + aumento
    print(f'Seu salário era de R${salario:.2f} \nO percentual para reajuste foi de 5%; \nO valor do aumento foi de R${aumento:.2f}; \nSeu novo salário será de R${novoSalario:.2f}!')

else:
    print('Valor Inválido!')
