algo = input('Digite algo com o seu teclado: ')
print(type(algo))
print('é numero?', algo.isnumeric())
print('é alfa? ', algo.isalpha())
print('é alfanumerico? ', algo.isalnum())

print('tá todo em maiusculo? ', algo.isupper())
print('tá em caixa baixa? ', algo.islower())

print('ele é ascii? ', algo.isascii())
print('é um valor decimal? ', algo.isdecimal())
print('é identificador? ', algo.isidentifier())
print('É possível imprimir? ', algo.isprintable())
print('É um espaço? ', algo.isspace())
print('É um título? ', algo.istitle())  # Tá capitalizada?
