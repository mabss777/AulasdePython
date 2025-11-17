import math
tamanho_arquivo = int(input('Digite qual o tamanho do arquivo para download (em MB): '))

velocidadeMbps = int(input('Digite a velocidade do link de internet (em Mbps): '))

mb = tamanho_arquivo * 8

tempo = mb / velocidadeMbps

minutos = math.ceil(tempo / 60)

print(f'O tempo aproximado dara o download do arquivo usando este link será de {minutos} minutos')


