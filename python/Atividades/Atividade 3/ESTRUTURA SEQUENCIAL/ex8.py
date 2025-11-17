ganhaHora = float(input('Digite o seu valor por hora trabalhada: '))
horaTrabalhada = float(input('Digite o total de horas trabalhadas: '))

salario = round((ganhaHora*horaTrabalhada),2)

print('Seu salário desse mês será de: R$',salario)