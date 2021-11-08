# A Confederação Nacional de Natação precisa de um program que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:

from datetime import date
ano_nascimento = int(input('Digite o ano em que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')
