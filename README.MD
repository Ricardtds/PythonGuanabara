# Curso Python Gustavo Guanabara 

## Modulo 1

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
        
> Manipulando Texto

    Fatiamento
        frase = 'Curso em Vídeo Python'
        frase[x1:x2]
        frase[x1:x2:step]
    
    Análise
        len(frase) > tamanho da frase
        frase.count('o') > conta a quantidade de letras o
        frase.count('o',0,13) > conta a quantidade de letras o com fatiamento
        frase.find('deo') > retorna a posição inicial
        'Curso' in frase > retorna True or False
        
    Transformação
        frase.replace('Python', 'Android') > Substitui o termo por outro.
        frase.upper() > Coloca o texto em caixa alta
        frase.lower() > Coloca o texto em caixa baixa
        frase.capitalize() > Coloca o primeiro caracter  em maiusculo
        frase.title() > Coloca a primeira letra de cada palavra em maiusculo.
        frase2 = '   Aprenda Python   '
        frase2.strip() > Remove os espaços em branco excedentes
        frase2 = frase2.rstrip() > Remove os espaços da direita
        frase2 = frase2.lstrip() > Remove os espaços da esquerda

    Divisão
        frase.split() > Separa as palavras.
        'termo'.join(frase) > Trasforma o array de palavras em string 
        separados pelo termo

    Print Diversas Linhas
        print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Ut venenatis condimentum urna. Sed quam arcu, blandit nec semper non. 
        Sed accumsan nec lectus sit amet consequat. Duis ultrices elementum 
        Fusce sit amet urna odio. Morbi facilisis ante eu viverra scelerisque. 
        Vestibulum pellentesque velit leo, quis varius est ornare in. 
        Aliquam sollicitudin tempor varius. Vestibulum ornare at tellus. ''')

> Condições

    Com o else = estrutura composta, sem else = estrutura simples.
    if condição:
        do it
        and it
        also it
    else:
        do it
        and it
        also it
    do it anyway

    Condição Simplificada
        print('txt1' if CONDIÇÃO else 'txt2')

> Cores no Terminal

    

> Anotações extras

    biblioteca time tem funções relacionadas ao tempo. Ex sleep
    Utiliza a tabulação, identação para blocos.
    Comentários de várias linhas:
    ''' comentário
        de várias
        linhas '''

> Cores no Python

    MODULO: COLORIZE (usa cores hexadecimal)
    padrão ANSI [escape sequence]

    \033[style;text;backm
    style
        0 None
        1 Bold
        4 Underline
        7 Negative
    text
        30 - branco
        31 - vermelho
        32 - verde
        33 - amarelo
        34 - azul
        35 - magenta
        36 - ciano
        37 - cinza
    back
        40 - branco
        41 - vermelho
        42 - verde
        43 - amarelo
        44 - azul
        45 - magenta
        46 - ciano
        47 - cinza 

## Modulo 2

>   Condições Aninhadas

    O Python aceita fazer x1 == x2 == x3
    if condição:
        bloco
    elif condição:
        bloco
    elif condição:
        bloco
    else:
        bloco