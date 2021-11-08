nome = str(input('Qual é o seu nome? '))
if nome == 'Ricardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Teu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu bem é bem normal.')
print('Tenha um bom dia {}'.format(nome))
