# Crie um programa onde o suário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos valores únicos digitados,
# em cordem crescente

numeros = list()
while True:
    while True:
        numero = int(input('Digite um valor: '))
        if numero in numeros:
            print('Valor repetido, não irei adicionar')
        else:
            numeros.append(numero)
            print(f'O valor {numero} foi adicionado a lista')
            break
    while True:
        opcao = str(input('Deseja continuar [S/N]: ')).strip().lower()
        if opcao in 'sn':
            break
    if opcao in 'n':
        break

numeros.sort()
print(numeros)
