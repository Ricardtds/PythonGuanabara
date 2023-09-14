# Estudo de Funções (parte 2)

+ Interactive Help
+ docstrings
+ Argumentos opcionais
+ Escopo de variáveis
+ Retorno de resultados

## Interactive Help
    help()

- DOCSTRINGS

    Uma explicação sobre o que a sua função realiza. Esta explicação é dada ao digitar help(nome_da_funcao)

    ```
    def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')   
    ```

- Parâmetros Opcionais

    São parametros os quais não há necessidades de serem passados pois ao serem omitidos receberão um valor default definido no escopo da função.

    ```
    def somar(a,b,c=0):
    s = a + b + c
    print(f'A oma vale {s}')

    somar(3,2,5)
    somar(8,4)
    ```
- Escopo de variáveis
    + Variável global
    ```
    def teste(b):
        global a
        a = 8
        b += 4
        c = 2
    a = 5
    teste(a)
    ```
    + Variável local

- Retornando Valores
    ```
    return
    ```