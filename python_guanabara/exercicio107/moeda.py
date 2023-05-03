def metade(n):
    return n/2


def dobro(n):
    return n * 2


def aumentar(n, p):
    '''
    ->funçao para calculo de aumento
    :param n: valor 
    :param p: taxa
    : return: valor acrescido da taxa
    '''
    valor = n + (n * (p / 100))
    return valor


def diminuir(n, p):
    valor = n - (n * (p / 100))
    return valor


def moeda(n):
    return f'R${n:.2f}'
       
