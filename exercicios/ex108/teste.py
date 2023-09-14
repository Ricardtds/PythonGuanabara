# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consga mostrar os valores como um valor monetário formatado.

import moeda

preco = float(input("Digite um preço: R$ "))
precoformatado = moeda.moeda(preco)
n = 10

print(f"A metade de R$ {precoformatado} é R$ {moeda.metade(preco, True)}")
print(f"o dobro de {precoformatado} é R$ {moeda.dobro(preco, True)}")
print(f"Aumentando {n}% de {precoformatado}, temos {moeda.aumentar(preco,n, True)}")
print(f"Diminuindo {n}% de {precoformatado}, temos {moeda.diminuir(preco,n, True)}")