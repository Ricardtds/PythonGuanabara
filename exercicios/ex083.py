# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = list()
abreparenteses = fechaparenteses = 0
expressao.append(str(input('Digite uma expressão na tua lista: ')))
for x in expressao[0]:
    if x == '(':
        abreparenteses += 1
    if x == ')':
        fechaparenteses += 1

if fechaparenteses == abreparenteses:
    print('É uma lista válida!')
else:
    print('Não é uma lista válida!')
