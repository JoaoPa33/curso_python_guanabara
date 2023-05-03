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


def resumo(n=0, aum=0, dim=0):
    '''
    -> funcao resumida
    :param n: recebe valor que será calculado
    :param aum: recebe valor percentual que será aumentado
    :param dim: recebe valor percentual que será diminuido
    '''
    print("-"* 40)
    #print(f'{"Resumo do valor":^40}')
    print("RESUMO DO VALOR".center(40))
    print("-"* 40)

    # topicos = {
    #     "Preço analisado:": moeda(n), 
    #     "Dobro do preço:":dobro(n, True),
    #     "Metade do preço:":metade(n, True), "de aumento:":aumentar(n, aum, True),
    #     "de redução:": diminuir(n, dim, True)
    #     }
    # topicos[f"{aum}% de aumento:"] = topicos.pop("de aumento:")
    # topicos[f"{dim}% de redução:"] = topicos.pop("de redução:")

    # for k, v in topicos.items():
    #     print(f"{k:<30}{v:>10}")
    
    # print("-"* 40)
    print(f'Preço analizado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(n, dim, True)}')
    print("-"* 40)




