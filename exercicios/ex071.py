# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a
# ser sacado(numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

sacar = int(input('Digite o valor que deseja sacar: '))
notas50 = sacar // 50
sobra50 = sacar % 50

notas20 = sobra50 // 20
sobra20 = sobra50 % 20

notas10 = sobra20 // 10
sobra10 = sobra20 % 10

notas1 = sobra10 // 1

print(f'Serão entregues:\n{notas50} notas de R$50,00')
print(f'{notas20} notas de R$20,00')
print(f'{notas10} notas de R$10,00')
print(f'{notas1} notas de R$1,00')
