def contar_c(s):
    """Funçao que conta caracteres de uma lista, atraves de um dicionario

    ex.
    >>>contar_c('banana')
    {'a': 3,'b': 1,'n': 2}

    :param s: string a ser contada
    :return: resultado
    """
    c_ordenados = sorted(s)
    c_anterior = c_ordenados[0]
    contagem = 1
    resultado = {}

    for c in c_ordenados[1:]:
        if c == c_anterior:
            contagem += 1
        else:
            resultado[c_anterior]=contagem
            c_anterior = c
            contagem = 1

    resultado[c_anterior]=contagem

    return resultado

if __name__ == '__main__':
    print(contar_c('banana'))