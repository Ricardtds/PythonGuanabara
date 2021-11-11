# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos


termo_a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0
s = termo_a1
qtd_termos = 10

while c < qtd_termos:
    print('{} -> '.format(s) if c != qtd_termos - 1 else '{}'.format(s), end="")
    s += razao
    c += 1
    if c == qtd_termos:
        print('')
        option = int(input('Deseja mostrar mais quantos termos: '))
        qtd_termos += option
print('{}'.format(qtd_termos))
