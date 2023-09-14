# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

# Faça também um progrmama que importe esse módulo e use algumas dessas funções.

import moeda

a = moeda.dobro(20)
b = moeda.metade(7)
c = moeda.aumentar(23,50)
d = moeda.diminuir(32,20)

print(f"a={a}, b={b}, c={c}, d={d}")