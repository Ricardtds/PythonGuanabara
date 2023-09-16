from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    

cabeçalho("SISTEMA DE CADASTRO", 42)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoaa', 'Sair do Sistema'])
    if resposta == 0:
        # listar pessoas cadastradas
        lerArquivo(arq)
    elif resposta == 1:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        cabeçalho("Saindo do sistema... Até logo!")
        sleep(1)
        break
    else:
        print("Digite uma opção válida!")