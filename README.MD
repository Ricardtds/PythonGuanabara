# Curso Python Gustavo Guanabara

> Tipos Primitivos

    int (O tipo inteiro)
    float (O tipo ponto flutuante)
    bool (True or False)
    srt (String)

> Saída de Dados

    print('A soma vale', s)
    print('A soma vale {}'.format(s))
    type(s) // Mostra o tipo de s

    s.isnumeric() // Diz se é possível converter o valor para um int
    s.isalpha // Diz se é alfa (sem números)
    s.isalnum // Diz se é alfanumerico
    s.isupper // Tá somente com letras maiusculas?
    s.islower // Tá somente com letras minusculas?
    s.isprintable // Se pode ser impresso.
    s.isspace // Se é um espaço.

> Operadores aritméticos

    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    ** Potência
    // Divisão inteira
    % Resto da divisão

> Ordem de Precedência

    1- ()
    2- ** # Ou pode usar o pow(x,y) <- Perde ordem de precedência
    3- * / // % Por ordem da esquerda para direita na expressão
    4- + -

> Alinhamentos e dicas no print

    Aula07a
    Número de casas no float > Linha 15 da aula07a
    Como não pular linhas entre 2 prints alterando o conteúdo > Linha 15 da aula07a
    Como quebrar a linha no meio do print: \n
    VARIÁVEL EM PYTHON ACEITA ACENTO
    
> Utilizando Modulos

    import - Comando para importar (importa tudo)
    from biblioteca import item, item2 (importa 1 item da biblioteca)
    math - biblioteca
        + ceil > arredondamento pra cima [item]
        + floor > arredondamento pra aixo [item]
        + trunc > truncamento [item]
        + pow > potencia [item]
        + sqrt > raiz quadrada [item]
        + factorial > calculo de fatorial [item]
        