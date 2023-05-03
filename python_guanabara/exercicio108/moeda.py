def metade(n=0):
    return n/2


def dobro(n=0):
    return n * 2


def aumentar(n=0, p=0):
    '''
    ->funçao para calculo de aumento
    :param n: valor 
    :param p: taxa
    : return: valor acrescido da taxa
    '''
    valor = n + (n * (p / 100))
    return valor


def diminuir(n=0, p=0):
    valor = n - (n * (p / 100))
    return valor


def moeda(n, p='R$'):
    return f'{p}{n:.2f}'.replace('.',',')
#def moeda(n, p ):
    #return f'R${n:.2f}'
       
