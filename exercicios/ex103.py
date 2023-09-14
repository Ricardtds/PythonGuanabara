# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha ido informado corretamente.

def ficha(nome,gols):
    print(f'O jogador {nome} marcou {gols} gols.')
    
nome = str(input("Digite o nome do jogador:") or "<desconhecido>")  
try:
    gols = int(input("Digite quanto gols foram feitos: ") or 0)
except:
    gols = 0
            
ficha(nome, gols)
