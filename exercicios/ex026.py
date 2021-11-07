# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A"

# Em que posição ela aparece pela primeria vez

# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()

print('Aparece a letra a {} vezes'.format(frase.count('A')))
print('Aparece primeiramente na posição {}'.format(frase.find('A')))
tamanho = len(frase)
print('Aparece pela ultima vez na posição {}'.format(tamanho - 1 - frase[::-1].find('A')))
print('Aparece pela ultima na posição {}'.format(frase.rfind('A')))