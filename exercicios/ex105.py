# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média das notas
# - A situação (opcional)

# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação do aluno
    :param n: uma ou mais notas do aluno (aceita várias)
    :param sit: vaor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = "BOA"
        elif r['media'] >= 5:
            r['situação'] = "RAZOÁVEL"
        else:
            r['situação'] = "RUIM"
    return r

resp = notas(5.5, 2.5, 10, 6.5, sit=True)
help(notas)
print(resp)