# Faça um programa que converta a temperatura.
C = float(input('Digite a temperatura em Celsius: '))
# C / 100 = (F - 32)/180
F = ((C / 100) * 180) + 32
print('A temperatura em F vale {}'.format(F))

# Onde C é a temperatura em graus Celsius e F, a temperatura em Fahrenheit. Ao simplificarmos a fórmula, temos: