# Refaça o Desafio 035 dos triângulos, acrescetando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: Todos os lados iguais.
# - Isósceles: dois lados iguais
# - Escaleno: Todos os lados diferentes

l1 = float(input('Digite a médida do lado 1 do triângulo: '))
l2 = float(input('Digite a medida do lado 2 do triângulo: '))
l3 = float(input('Digite a medida do lado 3 do triângulo: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('É possível fazer o triângulo.')
    if l1 == l2 == l3:
        print('É um triângulo equilátero')
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print('É um triângulo isósceles')
    # elif l1 != l2 != l3 != l1:
    else:
        print('É um triângulo escaleno')
else:
    print('Não é possível fazer o triângulo.')
