# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#EX: Digite o número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Digite um numero: '))
# milhar = int(numero/1000)
# centena = int(numero/100) - milhar*10
# dezena = int(numero/10) - centena*10 - milhar*100
# unidade = numero - dezena*10 - centena*100 - milhar*1000
#

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centena: {}'.format(centena))
print('milhar: {}'.format(milhar))

# Metodo da string
# Não é possível fazer ainda