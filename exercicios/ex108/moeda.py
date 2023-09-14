def aumentar(preco, taxa, f = False):
    res = preco * (1 + taxa/100)
    if f:
        return moeda(res)
    else:
        return res

def diminuir(preco, taxa, f = False):
    res = preco * (1 - taxa/100)
    if f:
        return moeda(res)
    else:
        return res

def dobro(preco, f = False):
    res = preco * 2
    if f:
        return moeda(res)
    else:
        return res

def metade(preco, f = False):
    res = preco /2
    if f:
        return moeda(res)
    else:
        return res
    
def moeda(preço, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.',',')