cor = [
    '\033[m',   #0 branco
    '\033[31m',  #1 vermelho
    '\033[32m',  #2 verde
    '\033[33m',  #3 amarelo
    '\033[34m',  #4 azul
    '\033[35m',  #5 seila, outra cor ai
]

def linha (tam = 40):
    return "-" * tam


def cabecalho(text, opcao =''):
    print(linha())
    if opcao:
        print(f'                {text} {opcao}') 
    else:    
        print(f'{text:^40}')
    print(linha())


def leiaInt(text, stilo=cor[3]):
    while True:
        try:
            opc = int(input(f"{stilo}{text}{cor[0]}"))
        except Exception:
            print(f'{cor[1]}Erro: não é um valor aceito{cor[0]}')
        else:
            return opc


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for index,itens in enumerate(lista):
        print(f'{cor[3]}{index + 1}{cor[0]} - {cor[4]}{itens}{cor[0]}')
    print(linha()) 
    '''
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    '''    
    opc = leiaInt('Sua Opção: ')
    return opc