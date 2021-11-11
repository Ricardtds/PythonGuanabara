# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] sair do programa

# Seu programa deverá realizar a opção solicitada em cada caso

option = 4
while option != 5:
    if option == 4:
        n1 = float(input('Digite o valor 1: '))
        n2 = float(input('Digite o valor 2: '))
    print('''O que Deseja Fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] sair do programa''')
    option = int(input('Digite sua opção: '))
    if option == 1:
        resultado = n1 + n2
    elif option == 2:
        resultado = n1 * n2
    elif option == 3:
        resultado = max(n1, n2)
    if option == 3 or option == 2 or option == 1:
        print('O resultado da operação foi: {}'.format(resultado))
