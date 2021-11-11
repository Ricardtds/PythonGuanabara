# Faça um programa que mostre a tabuada de vários números, para cada valor digitado pelo usuário. o programa será
# interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um número não negativo: '))
    if numero < 0:
        break
    for x in range(1, 11):
        print(f'{numero} x {x} = {numero*x}')
