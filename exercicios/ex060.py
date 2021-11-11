# Faça um programa que leia um número qualquer e mostre o seu fatorial

# EX: 5! = 5 x 4 x 3 x 2 x 1

numero = int(input('Digite o número: '))
numero = abs(numero)
resultado = 1

while numero >= 1:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    resultado *= numero
    numero -= 1

print(resultado)
