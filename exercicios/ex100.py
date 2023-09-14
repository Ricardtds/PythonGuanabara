import random
import time

numeros = []


def sorteia(lst):
    a = 0
    while a<5:
        lst.append(random.randint(0,10))
        a+=1

def somaPar(lst):
    valordePares = 0
    for valor in lst:
        if (valor%2==0):
            valordePares+=valor
    print(valordePares)

def imprimirLista(lst):
    for val in lst:
        print(val, end=" ")
        time.sleep(.5)
    print()

sorteia(numeros)
imprimirLista(numeros)
somaPar(numeros)