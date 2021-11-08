# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o salário do comprador? '))
anos_pagamento = int(input('Em quantos anos irá pagar? '))

prestacao_mensal = valor_casa / (anos_pagamento * 12)

if prestacao_mensal > (salario_comprador*0.3):
    print('Emprestimo negado')
else:
    print('Emprestimo Aprovado. Você deverá pagar R${:.2f} por mês'.format(prestacao_mensal))
