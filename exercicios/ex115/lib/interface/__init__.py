def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except ValueError:
            print("Digite um valor inteiro válido.")
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return 2
        except Exception as erro:
            print(f"O erro foi: {erro.__class__}")
        else:
            return a

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt, tam=42):
    print(linha(tam))
    print(txt.center(tam))
    print(linha(tam))
    
def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 0
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Sua Opção: ")
    return opc