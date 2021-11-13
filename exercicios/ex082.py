# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares
# digitados respectivamente.

# Ao final, mostre o conteúudo das três listas geradas.

lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar [S/N]: ')).strip()[0]
    if opcao in 'Nn':
        break
listapar = list()
listaimpar = list()

for x in lista:
    if x % 2 == 0:
        listapar.append(x)
    else:
        listaimpar.append(x)

print(f'A lista digitada foi: {lista}')
print(f'Os valores pares da lista foram: {listapar}')
print(f'Os valores impares da lista foram: {listaimpar}')
