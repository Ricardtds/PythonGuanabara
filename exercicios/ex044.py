# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e a condição de pagamento:

# - À vista Dinheiro/Cheque: 10% de desconto

# - À vista no cartão 5% de desconto

# Em até 2x no cartão: preço normal

# 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: R$'))

print('''Qual Será a forma de pagamento?
[1] - À vista dinheiro/cheque
[2] - À vista no cartão
[3] - Em até 2x no cartão
[4] - 3x ou mais no cartão''')

metodo = int(input('A sua escolha: '))

if metodo == 1:
    print('Você pagará R${:.2f} pelo produto.'.format(valor*0.9))
elif metodo == 2:
    print('Você pagará R${:.2f} pelo produto.'.format(valor*0.95))
elif metodo == 3:
    print('Você pagará R${:.2f} pelo produto.'.format(valor))
elif metodo == 4:
    print('Você pagará R${:.2f} pelo produto.'.format(valor*1.2))
else:
    print('Opção invalida!')
