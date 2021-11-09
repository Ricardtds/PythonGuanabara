# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando o laço for

numero = int(input('Digite o número que você precisa da tabuada: '))

for x in range(0, 11):
    print('{} x {} = {}'.format(numero, x, numero*x))