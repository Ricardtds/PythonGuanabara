# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('Você foi multado')
    multa = (velocidade - 80) * 7
    print('O valor de sua multa é R${:.2f}'.format(multa))
