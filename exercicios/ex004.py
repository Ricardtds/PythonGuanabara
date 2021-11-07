algo = input('Digite algo com o seu teclado: ')
print(type(algo))
print('é numero? \033[35m', algo.isnumeric(), '\033[m')
print('é alfa? \033[35m', algo.isalpha(), '\033[m')
print('é alfanumerico? \033[35m', algo.isalnum(), '\033[m')

print('tá todo em maiusculo? \033[36m', algo.isupper(), '\033[m')
print('tá em caixa baixa? \033[36m', algo.islower(), '\033[m')

print('ele é ascii? \033[31m', algo.isascii(), '\033[m')
print('é um valor decimal? \033[32m', algo.isdecimal(), '\033[m')
print('é identificador? \033[32m', algo.isidentifier(), '\033[m')
print('É possível imprimir? \033[31m', algo.isprintable(), '\033[m')
print('É um espaço? \033[32m', algo.isspace(), '\033[m')
print('É um título? \033[31m', algo.istitle(), '\033[m')  # Tá capitalizada?
