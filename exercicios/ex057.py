# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores "M"
# ou "F". Caso esteja eerado, peça a digitação novamente até ter um
# valor correto.

sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(
        input('Dados inválidos. Digite o seu sexo [M/F]: ')).strip().upper()[0]
    print(sexo)
