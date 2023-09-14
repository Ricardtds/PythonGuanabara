# Faça um mini-sistema que utilize o InteractiveHelp do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

# OBS: use cores.
c = ('\033[m',  # 0 - sem cores 
     '\033[0;30;41m',   # 1 - vernmelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m',      # 6 - branco
     );
def ajuda(com,cor=0):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[cor])
    help(com)
    print(c[0])
    
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print("~"*tam)
    print(f"  {msg}  ")
    print("~"*tam)
    print(c[0])

# Programa principal
comando = ''
while True:
    titulo("Sistema de ajuda PyHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando,3)
titulo("Até Logo!", 2)