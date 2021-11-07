# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.

# Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: '))

if salario > 1250:
    novosalario = salario * 1.10
else:
    novosalario = salario * 1.15

print('Teu novo salario é de R$ {:.2f}'.format(novosalario))
