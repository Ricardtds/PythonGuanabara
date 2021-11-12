# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.

# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for x in range(0, len(produtos), 2):
    # print('{:.<20} {:.2f and >6}'.format(produtos[x], produtos[x+1]))
    print(f'{produtos[x]:.<28}R$ {produtos[x+1]:.2f}')
print('-'*40)