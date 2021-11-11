# Crie um programa que leia a idade o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos

# B) Quantos homens foram cadastrados

# C) Quantas mulheres com menos de 20 anos.

contadormaiores = contadorhomens = mulheresjovens = 0

while True:
    while True:
        idade = int(input('Digite a sua idade: '))
        if idade >= 0:
            break
    while True:
        sexo = str(input('Digite o seu sexo [F/M]: ')).strip().lower()[0]
        if sexo in 'mf':
            break
    if idade > 18:
        contadormaiores += 1
    if sexo == 'm':
        contadorhomens += 1
    if idade < 20 and sexo == 'f':
        mulheresjovens += 1

    while True:
        continuar = str(input('Deseja cadastrar alguém [S/N]: ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar == 'n':
        break

print(f'Tivemos {contadormaiores} pessoas com mais de 18 anos!')
print(f'Tivemos {contadorhomens} homens cadastrados!')
print(f'Tivemos {mulheresjovens} mulheres com menos de 20 anos!')
