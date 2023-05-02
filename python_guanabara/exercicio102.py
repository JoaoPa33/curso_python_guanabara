def fatorial(n, show=False):
    '''
    -> Funçao que retorna o valor fatorial
    :param n: valor que deseja ser calculado
    :param show: mostra que o calculo será mostrado
    :return : mostra o calculo final de n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(c," x ", end="")
            else:
                print(c," = ", end="")
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True))
help(fatorial)
    