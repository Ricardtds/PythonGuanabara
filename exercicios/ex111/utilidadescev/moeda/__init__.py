def aumentar(preço, taxa, f = False):
    res = preço * (1 + taxa/100)
    if f:
        return moeda(res)
    else:
        return res

def diminuir(preço, taxa, f = False):
    res = preço * (1 - taxa/100)
    if f:
        return moeda(res)
    else:
        return res

def dobro(preço, f = False):
    res = preço * 2
    if f:
        return moeda(res)
    else:
        return res

def metade(preço, f = False):
    res = preço /2
    if f:
        return moeda(res)
    else:
        return res
    
def moeda(preço, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.',',')

def resumo(preço, aumento, redução):
    res = dict()
    res["metade"] = metade(preço, True)
    res["dobro"] = dobro(preço, True)
    res["aumento"] = aumentar(preço, aumento, True)
    res["redução"] = diminuir(preço, redução, True)
    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)
    print(f"Preço analisado:\t {moeda(preço)}")
    print(f"Dobro do preço: \t {res['dobro']}")
    print(f"Metade do preço:\t {res['metade']}")
    print(f"{aumento}% de aumento: \t {res['aumento']}")
    print(f"{redução}% de redução: \t {res['redução']}")
    print("-"*40)