def f_contar_c(s): #criar função que conta casacteres da string 's'(s)
    """Função contar caracteres de uma string
    ##Quais são os caracteres de uma string, e quantas vezes cada caracter aparece na mesma?
    Ex:

    >>> f_contar_c('fabricio')
    a: 1
    b: 1
    c: 1
    f: 1
    i: 2
    o: 1
    r: 1
    >>> f_contar_c('araujo')
    a: 2
    j: 1
    o: 1
    r: 1
    u: 1

    :param s: string a ser contada

    """
    f_c_ordenados = sorted(s) #f = função, c = caracteres, s = string
    f_def_c_ant = f_c_ordenados[0] #[0] = repr. 1º c #manter ref p c anterior da s enqto o c anterior for = ao c corrente, somar num de vez q esse c aparece
    valor_c = 1
    for c in f_c_ordenados[1:]: #iteração dos c subsequntes, q é a partir de [1] (no caso o 1º c é o [0], o 2º c é [1])
        if c == f_def_c_ant:
            valor_c += 1
        else: #então se não houver nenhuma das situaçõaes acima:
            print(f'{f_def_c_ant}: {valor_c}') #eu vou imprimir o c ant e o seu valor
            f_def_c_ant = c #o c anterior passa a ref o c atual
            valor_c = 1 #valor do novo c da lista
    print(f'{f_def_c_ant}: {valor_c}') #ref ao ultimo c


if __name__ == '__main__': #
    f_contar_c('fabricio')
    print() #serve para pular linha
    f_contar_c('araujo')
