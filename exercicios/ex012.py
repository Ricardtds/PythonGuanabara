# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))
print('O valor do produto é {:.2f}\nO valor com desconto é {:.2f}'.format(preco, preco*0.95))
