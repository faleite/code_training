def fizz_buzz(n: int):
    """
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    # div 2 = fizz, div 3 = buzz
    :param n:
    :return:
    """
    for i in range(1, n + 1): #i=1 n=6
        resultado = ''

        if i % 2 == 0:
            resultado = 'fizz'
        if i % 3 == 0:
            resultado += 'buzz'

        print(resultado if resultado != '' else i) # 1 fizz 3 fizz 5 fizz


