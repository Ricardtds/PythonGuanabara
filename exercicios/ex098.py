import time
def contador(inicio, fim, passo):
    a = inicio
    passo = abs(passo)
    if(passo==0):
        passo = 1
    if(inicio < fim):
        while a <= fim:
            print(a, end=' ')
            a += passo
            time.sleep(0.1)
    else:
        while a >= fim:
            print(a, end=' ')
            a -= passo
            time.sleep(0.1)
    print("Fim!")
    
contador(0, 10, 1)
contador(10, 0, 2)

print("Digite o valor do inicio:")
a = int(input("A"))

print("Digite o valor do fim:")
b = int(input("Fim"))

print("Digite o valor do passo:")
c = int(input("Passo"))

contador(a, b, c)