# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

# Faça também um progrmama que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input("Digite um preço: R$ "))
n = 10

print(f"A metade de R$ {preco} é R$ {moeda.metade(preco)}")
print(f"o dobro de R$ {preco} é R$ {moeda.dobro(preco)}")
print(f"Aumentando {n}% de {preco}, temos R$ {moeda.aumentar(preco,n)}")
print(f"Diminuindo {n}% de {preco}, temos R$ {moeda.diminuir(preco,n)}")