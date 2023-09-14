# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, so que fazendo a validação para aceitar apenas um valor númerico.

# Ex:
# n = leiaInt('Digite um n')

def leiaInt(frase):
    while True:
        try:
            num = int(input(frase))
            break
        except ValueError:
            print("\033[0;31mPor favor insira um número inteiro.\033[m")
    
n = leiaInt("Digite um valor: ")