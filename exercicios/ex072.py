# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.

# Seu programa deverá ler um número pelo telcado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        numero = int(input('Por favor digite um número de 0 até 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'O valor em extenso do número é: {numeros[numero]}')
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
