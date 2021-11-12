# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

valores = (int(input('Digite o valor[1]: ')),
           int(input('Digite o valor[2]: ')),
           int(input('Digite o valor[3]: ')),
           int(input('Digite o valor[4]: ')))

print(f'Você digitou os valores: {valores}')
print(f'Tivemos um total de {valores.count(9)} valores 9')
print(f'O valor 3 apareceu primeiro na posição {valores.index(3)+1}' if valores.count(3) > 0 else 'Não teve o valor 3')
print('Os valores pares foram: ', end='')
for x in valores:
    if x % 2 == 0:
        print(x, end=' ')
