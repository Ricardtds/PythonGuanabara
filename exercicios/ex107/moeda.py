def aumentar(preco, taxa, f = False):
    res = preco * (1 + taxa/100)
    return res

def diminuir(preco, taxa, f = False):
    res = preco * (1 - taxa/100)
    return res

def dobro(preco, f = False):
    res = preco * 2
    return res

def metade(preco, f = False):
    res = preco /2
    return res