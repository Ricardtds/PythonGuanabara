# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Quantos dias dias? '))
km = float(input('Quantos km foram rodados?'))
print('Voce alugou por {} dias e rodou {} kms\n O valor total é de {}'.format(dias,km,(dias*60 + km * 0.15)))
