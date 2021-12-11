# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário se
# por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

year = datetime.today().year
pessoa = {
    'nome': str(input('Digite o teu nome: ')),
    'idade': year - int(input('Digite o teu ano de nascimento: ')),
    'carteira_trabalho': int(input('Carteira de trabalho (0 não tem): ')),
}
if pessoa['carteira_trabalho'] != 0:
    pessoa['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = 35 - \
        (year - pessoa['ano_contratacao']) + pessoa['idade']

print()
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')
