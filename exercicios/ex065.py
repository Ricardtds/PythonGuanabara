# Crie um programa que leia vários núumeros inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores


option = 's'
count = somatorio = 0

while option in 'Ss':
    numero = int(input('Digite um número inteiro: '))
    if count == 0:
        menor = maior = numero
    else:
        if menor > numero:
            menor = numero
        if maior < numero:
            maior = numero
    count += 1
    somatorio += numero
    option = str(input('Quer continuar? '))

media = somatorio / count
print('A média foi de: {}\nO menor valor lido: {}\nO maior valor lido: {}'
      .format(media, menor, maior))
