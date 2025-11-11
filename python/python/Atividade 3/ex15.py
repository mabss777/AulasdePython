ganhaHora = float(input('Digite o seu valor por hora trabalhada: '))
horaTrabalhada = float(input('Digite o total de horas trabalhadas: '))

salarioBruto = round((ganhaHora*horaTrabalhada),2)
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
impostoRenda = salarioBruto * 0.11
salarioLiquido = salarioBruto - (inss + sindicato + impostoRenda)

print('Seu salário bruto é de R$',salarioBruto)
print('Você pagou ao INSS o valor de R$', inss)
print('Você pagou ao sindicato o valor de R$', sindicato)
print('Seu salário líquido será de R$',salarioLiquido )
