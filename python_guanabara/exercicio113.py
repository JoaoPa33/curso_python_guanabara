def leiaInt(msg):
    while True:
        try:
            i = int(input(f"{msg}"))
            #break ( se colocar o break a identaçao tem que ser alterada ATENCAO)
        except (ValueError, TypeError):
            print(f"\033[31mErro: por favor, digite um numero inteiro\033[m")
        except (KeyboardInterrupt):
            print(f"\033[31mErro: entrada de valor interrompida pelo usuario.\033[m")
            return 0
        else:
            return i


def leiaFloat(msg):
    while True:
        try:
            r = float(input(f"{msg}"))
        except Exception:
            print(f"\033[31mErro: por favor,digite um numero inteiro\033[m")
        else:
            return r


i = leiaInt('Digite um valor inteiro:')
r = leiaFloat('Digite um valor real:')
print(f"O valor inteiro é {i} e o valor real {r}")
