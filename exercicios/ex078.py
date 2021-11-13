# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

# No final, mostre quak foi o maior e o menor valor digitado e as suas respectivas posições
# na lista

valores = list()
for x in range(5):
    valores.append(int(input('Digite um valor: ')))

maior = max(valores)
menor = min(valores)

posmaior = list()
posmenor = list()

for pos, item in enumerate(valores):
    if maior == item:
        posmaior.append(pos)
    if menor == item:
        posmenor.append(pos)
print(valores)
print(f'O maior valor foi {maior} e ele apareceu nas posições {posmaior}')
print(f'O menor valor foi {menor} e ele apareceu nas posições {posmenor}')
