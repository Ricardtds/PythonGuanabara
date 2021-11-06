# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
numero = float(input('Digite um numero '))
print('Você digitou {}\nO dobro dele é {}\nO triplo dele é {}\nA raíz quadrada dele é {:.2f}'.format(numero, numero*2, numero*3, numero**(1/2)))
