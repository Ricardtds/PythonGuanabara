# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# A) Qual é o total gasto na compra

# B) Quantos produtos custam mais de R$1000,00

# C) Qual é o nome do produto mais barato.
total = produtoscaros = 0
while True:

    nome_produto = str(input('Digite o nome do produto: '))
    while True:
        preco_produto = float(input('Digite o valor do produto: '))
        if preco_produto > 0:
            break
    if total == 0:
        produtobarato = nome_produto
        precoprodutobarato = preco_produto
    else:
        if precoprodutobarato > preco_produto:
            precoprodutobarato = preco_produto
            produtobarato = nome_produto
    total += preco_produto
    if preco_produto > 1000:
        produtoscaros += 1

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()
        if continuar == 's' or continuar == 'n':
            break
    if continuar == 'n':
        break

print(f'O total gasto foi de R${total:.2f}')
print(f'Tivemos {produtoscaros} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {produtobarato} custando R${precoprodutobarato:.2f}')
