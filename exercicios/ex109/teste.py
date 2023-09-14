# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por eles vi ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input("Digite um preço: R$ "))
precoformatado = moeda.moeda(preco)
n = 10

print(f"A metade de R$ {precoformatado} é R$ {moeda.metade(preco, True)}")
print(f"o dobro de {precoformatado} é R$ {moeda.dobro(preco, True)}")
print(f"Aumentando {n}% de {precoformatado}, temos {moeda.aumentar(preco,n, True)}")
print(f"Diminuindo {n}% de {precoformatado}, temos {moeda.diminuir(preco,n, True)}")
