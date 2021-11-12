# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
            'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for pos, item in enumerate(palavras):
    print(f'A palavra {item} tem as vogais: ', end='')
    for x in item:
        if x in 'AaEeIiOoUu':
            print(x, end=' ')
    print()
