def area(l, c):
    m = l * c
    print(f"A área é de um terreno com {l}m de largura com {c}m de comprimento é de {m:.2f}m²")


def cabecalho(titulo):
    print("=-=" * 20)
    print(f'{titulo:^60}')
    print("=-=" * 20)


#Programa principal
cabecalho("MEDINDO ÁREA")
while True:
    try:
        l = float(input("Qual é a LARGURA da área?"))
        break
    except ValueError:
        print("Erro. Digite um numeral")
while True:
    try:
        c = float(input("Qual o COMPRIMETO da área?"))
        break
    except ValueError:
        print("Erro. Digite um número")
area(l , c)





