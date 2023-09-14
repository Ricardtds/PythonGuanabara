import time
def maior(*parametros):
    if(len(parametros) != 0):
        maior = parametros[0]
        for parametro in parametros:
            print(parametro, end=" ")
            time.sleep(0.25)
            if maior < parametro:
                maior = parametro
        print()
        print(f'Foram informados {len(parametros)} valores e o maior foi: {maior}')
    else:
        print("Não foram passados parametros")
    
maior(135,14125,12521,6125,2)
maior(2,4, 7, 0)