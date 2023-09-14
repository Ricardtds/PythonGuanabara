# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO na eleições.

def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade > 70:
        resposta = "OPCIONAL"
    elif idade >= 16 and idade < 18:
        resposta = "OPCIONAL"
    elif idade < 16:
        resposta = "NEGADO"
    else:
        resposta = "OBRIGATORIO"
    return f"Você tem {idade} anos e o vote é {resposta}"

nascimento = int(input("Digite a idade em que nasceu: "))
print(voto(nascimento))