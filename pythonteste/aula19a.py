dados = dict()
dados = {'Nome': 'Pedro', 'idade': 25}
print(dados)
dados['Sexo'] = 'Masculino'
print(dados)
del dados['idade']
print(dados)
filme = {
    'Titulo': 'Star Wars',
    'Ano': 1977,
    'Diretor': 'George Lucas'
}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
print()
for k, v in filme.items():
    print(f'O {k} é {v}')
filme2 = {
    'Titulo': 'Avengers',
    'Ano': 2012,
    'Diretor': 'Joss Whedon'
}
locadora = list()
locadora.append(filme)
locadora.append(filme2)
print(locadora)
