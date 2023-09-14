def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno {largura}x{comprimento} vale: {area} metros².')
    
print('Digite a largura do terreno(m): ')
largura = float(input("Largura(m)"))
print('Digite o comprimento do terreno(m): ')
comprimento = float(input("Comprimento(m)"))
area(largura, comprimento)