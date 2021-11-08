# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('Escolha uma opção:\n1- Pedra\n2- Papel\n3- Tesoura')

itens = ('Pedra', 'Papel', 'Tesoura')
opcao_computador = randint(1, 3)
opcao = int(input('Digite a opcão: '))
if 0 < opcao < 4:
    if ((opcao_computador == 1) and (opcao == 1)) \
            or ((opcao_computador == 2) and (opcao == 2)) \
            or ((opcao_computador == 3) and (opcao == 3)):
        print('Eu também escolhi {}, então empatamos'.format(itens[opcao_computador - 1]))
    elif ((opcao_computador == 1) and (opcao == 2)) \
            or ((opcao_computador == 2) and (opcao == 3)) \
            or ((opcao_computador == 3) and (opcao == 1)):
        print('Droga! Eu escolhi {} então perdi.'.format(itens[opcao_computador - 1]))
    else:
        print('Ahá, Eu escolhi {}, então venci!'.format(itens[opcao_computador - 1]))
else:
    print('Opção Invalida!')
