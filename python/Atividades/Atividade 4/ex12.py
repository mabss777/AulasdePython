import math

valorHora = float(input('Digite qual o valor da sua hora de trabalho: '))
horasTrabalhadas = float(input('Digite o seu total de horas trabalhadas: '))

salarioBruto = horasTrabalhadas * valorHora
inss = (salarioBruto * 0.1) 
fgts = salarioBruto * 0.11

if salarioBruto <= 900:
    total_descontos = inss + fgts
    salario_liquido = salarioBruto - total_descontos
    print(f'Sálario Bruto: ({valorHora} * {horasTrabalhadas}): R${salarioBruto:.2f} \n(-)IR: ISENTO \n(-)INSS(10%): R${inss:.2f} \nFGTS(11%): R${fgts:.2f} \nTotal de descontos: R${total_descontos:.2f} \nSalário Líquido: R${salario_liquido:.2f}')

elif salarioBruto <= 1500:
    imposto_renda = salarioBruto * 0.05
    total_descontos = inss + imposto_renda
    salario_liquido = salarioBruto - total_descontos
    print(f'Sálario Bruto: ({valorHora} * {horasTrabalhadas}): R${salarioBruto:.2f} \n(-)IR(5%): R${imposto_renda:.2f} \n(-)INSS(10%): R${inss:.2f} \nFGTS(11%): R${fgts:.2f} \nTotal de descontos: R${total_descontos:.2f} \nSalário Líquido: R${salario_liquido:.2f}')

elif salarioBruto <= 2500:
    imposto_renda = salarioBruto * 0.1
    total_descontos = inss + imposto_renda
    salario_liquido = salarioBruto - total_descontos
    print(f'Sálario Bruto: ({valorHora} * {horasTrabalhadas}): R${salarioBruto:.2f} \n(-)IR(10%): R${imposto_renda:.2f} \n(-)INSS(10%): R${inss:.2f} \nFGTS(11%): R${fgts:.2f} \nTotal de descontos: R${total_descontos:.2f} \nSalário Líquido: R${salario_liquido:.2f}')

elif salarioBruto > 2500:
    imposto_renda = salarioBruto * 0.2
    total_descontos = inss + imposto_renda
    salario_liquido = salarioBruto - total_descontos
    print(f'Sálario Bruto: ({valorHora} * {horasTrabalhadas}): R${salarioBruto:.2f} \n(-)IR(20%): R${imposto_renda:.2f} \n(-)INSS(10%): R${inss:.2f} \nFGTS(11%): R${fgts:.2f} \nTotal de descontos: R${total_descontos:.2f} \nSalário Líquido: R${salario_liquido:.2f}')

else:
    print('Valor inválido!')