# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt, hypot

catetooposto = float(input('Diigte o valor do cateto oposto: '))
catetoadjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt((pow(catetooposto, 2) + pow(catetoadjacente, 2)))

print('A hipotenusa vale {}'.format(hipotenusa))

print(hypot(catetooposto, catetoadjacente))
