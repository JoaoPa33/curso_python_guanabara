def metade(n=0, form=False):
    valor = n/2 
    #return valor if form == False else moeda(valor)
    if form == False:
        return valor
    else:
        return moeda(valor)


def dobro(n=0, form=False):
    valor = n * 2
    #return valor if not form else moeda(valor) 
    if not form:
        return valor
    else:
        return moeda(valor)

def aumentar(n=0, p=0, form=False):
    '''
    ->funçao para calculo de aumento
    :param n: valor 
    :param p: taxa
    : return: valor acrescido da taxa
    '''
    valor = n + (n * (p / 100))
    #return valor if form is False else moeda(valor)
    if form is False:
        return valor
    else:
        return moeda(valor)


def diminuir(n=0, p=0, form=False):
    valor = n - (n * (p / 100))
    return valor if form is False else moeda(valor)


def moeda(n, p='R$'):
    return f'{p}{n:.2f}'.replace('.',',')
#def moeda(n, p ):
    #return f'R${n:.2f}'
       
