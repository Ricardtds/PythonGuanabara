# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamda resumo(), que mostre na tela algumas informações eradas pelas funções que já temos no módulo criado até aqui.

from utilidadescev import moeda, dado

p = dado.leiaDinheiro("Digite o preço: R$ ")

moeda.resumo(p, 35, 22)