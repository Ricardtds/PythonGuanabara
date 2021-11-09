# Faça um programa que calcule a soma de todos os números ímpares que são multiplos de três e que se encontram
# no intevalo de 1 até 500
s = 0
count = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        s += x
        count += 1

print(s)
print(count)
