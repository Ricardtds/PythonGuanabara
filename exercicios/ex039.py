# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo.
from datetime import date

dia_semana, dia_atual = date.today().weekday(), date.today().day
mes_atual, ano_atual = date.today().month, date.today().year

ano_nascimento = int(input('Digite o ano em que você nasceu: '))
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Ainda não é hora de se alistar, espere mais {} ano(s)'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Ainda não se alistou? Está {} anos atrasado.'.format(idade-18))
