valorHora = float(input('Digite qual o valor da sua hora de trabalho: '))
horasTrabalhadas = float(input('Digite o seu total de horas trabalhadas: '))

salarioBruto = horasTrabalhadas * valorHora

if salarioBruto <= 900:
    print(f'Sálario Bruto: ({valorHora} * {horasTrabalhadas}): R${salarioBruto:.2f} \n(-)IR: ISENTO')
