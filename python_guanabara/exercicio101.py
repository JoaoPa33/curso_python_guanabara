from datetime import date


def voto(a):
    data = date.today().year
    idade_atual = data - a
    if idade_atual < 16:
        print(f"\033[31mNEGADO\033[m. Sua idade atual é de {idade_atual} anos")
    elif 16 <= idade_atual <18 or idade_atual >65:
        print(f"\033[33mFacultativo\033[m. Sua idade é de {idade_atual} anos")
    else:
        print(f"\033[32mObrigatorio\033[m. Sua idade é de {idade_atual} anos")


#Programa principal
while True:
    try:
        nasc = int(input("Em que ano você nasceu: "))
        break
    except ValueError:
        print("Digite um valor valido")
voto(nasc)