# Escreva um programa que leia um valor em metros eo exiba convertido em centimetros e milimetros
metros = float(input('Digite quantos metros deseja: '))
print('Voce digitou \033[32m{}\033[m metros\n'
      'Equivale a \033[34m{:.0f}\033[mcm\n'
      'Equuivale a \033[34m{:.0f}\033[mmm'
      .format(metros, metros*100, metros*1000)
      )
