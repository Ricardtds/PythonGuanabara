# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamdo show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num,show = False):
    f = 1
    for c in range(num, 1, -1):
        if show:
            print(f'{c}', end=' x ')
        f *= c
    print(f'1 = {f}')

n = int(input("Digite um número inteiro: "))
fatorial(n, True)