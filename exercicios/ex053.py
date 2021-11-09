# Crie um programa que leia uma frase qualque e diga se ela é um palíndromo, desconsiderando os
# Espaçcos.

# EX: APOS A SOPA
# Você lê igual de trás pra frente
#
# frase = str(input('Digite uma frase: ')).strip().lower().split()
# frasejunta = ''.join(frase)
#
# print(frasejunta)
#
# frasejuntarevertida = ''.join(list(reversed(frasejunta)))
#
# print(frasejuntarevertida)
# if(frasejunta == frasejuntarevertida):
#     print('É um palíndromo!')

frase = str(input('Digite uma frase: ')).lower().strip()
frase_invertida = ''
for x in range(len(frase)-1, -1, -1):
    frase_invertida += frase[x]

print('Frase Normal: {}'.format(frase))
print('Frase Invertida: {}'.format(frase_invertida))

if frase == frase_invertida:
    print('É um palíndromo!')
