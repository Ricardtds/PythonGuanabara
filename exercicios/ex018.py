# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite um angulo: '))
angulo = math.radians(angulo)
print(angulo)
print('O seno vale {:.2f}\n'
      'O Cosseno vale {:.2f}\n'
      'A Tangente vale {:}'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))
