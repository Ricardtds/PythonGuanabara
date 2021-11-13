# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, mostre:

# A) Quantos números foram digitados.

# B) A lista de valores, ordenada de forma decrescente.

# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar [S/N]? ')).strip().lower()
    if opcao in 'n':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
print(f'Os números digitados foram: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado!')
