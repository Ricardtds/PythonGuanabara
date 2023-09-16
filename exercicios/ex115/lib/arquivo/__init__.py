import lib.interface

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print("Houve um erro na criaão do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")
    finally:
        a.close()
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler arquivo.")
    else:
        lib.interface.cabeçalho("PESSOAS CADASTRADAS")
        # print("Idade".ljust(33), end="")
        # print("Anos")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f'{dado[0]:<30}\t{dado[1]:>3} anos')
    finally:
        a.close()
        
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()