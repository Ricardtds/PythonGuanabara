# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
numero = float(input('Digite um numero '))
print('Você digitou: \033[36m{}\033[m\n'
      'O dobro dele é \033[36m{}\033[m\n'
      'O triplo dele é \033[36m{}\033[m\n'
      'A raíz quadrada dele é \033[36m{:.2f}\033[m'
      .format(numero, numero*2, numero*3, numero**(1/2))
      )
