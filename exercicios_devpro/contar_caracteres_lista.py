def contar_c(s):
    """Função que conta caracteres de uma lista
    ex: "Quais são os caracteres e quantas vezes ele aparece, time video 3:35"
    >>> contar_c('leite')
    e: 2
    i: 1
    l: 1
    t: 1

    :param s: string a ser contada
    """
    c_ordenados = sorted(s)
    c_anterior = c_ordenados[0]
    contagem =  1

    for c in c_ordenados[1:]:
        if c == c_anterior:
            contagem += 1
        else:
            print(f'{c_anterior}: {contagem}')
            c_anterior = c
            contagem = 1
    print(f'{c_anterior}: {contagem}')

if __name__ == '__main__':
    contar_c('leite')





