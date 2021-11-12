# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.

# Seu programa deverá ler um número pelo telcado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número de 0 até 20: '))
    if 0 <= numero <= 20:
        break

print(numeros[numero])
