# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status, de acordo
# com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

IMC = peso / altura**2
print('Seu IMC vale: {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso!')
elif IMC <= 25:
    print('Você está no peso ideal')
elif IMC <= 30:
    print('Você está com sobrepeso')
elif IMC <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida')