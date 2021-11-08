# Escreva um programa que leia um número inteiro e peça para o usuário eescolher qual será a base de conversão:
# 1 Para binário
# 2 Para Octal
# 3 Para hexadecimal

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
 [1] Binária
 [2] Octal
 [3] Hexadecimal''')
opcao = int(input('Vai converter para qual base? '))

if opcao == 1:
    print('Você digitou {}, ele vale {:b} na base binária'.format(numero, numero))
elif opcao == 2:
    print('Você digitou {}, ele vale {:o} na base octal'.format(numero, numero))
elif opcao == 3:
    print('Você digitou {}, ele vale {:X} na base hexadecimal'.format(numero, numero))
else:
    print('Opção inválida')

