from time import sleep
cores = (
    '\033[m',  # 0 nenhuma
    '\033[0;30;41m',  # 1 vermelhos
    '\033[0;30;42m',  # 2 verde
    '\033[0;30;43m',  # 3 amarelo
    '\033[0;30;44m',  # 4 azul
    '\033[0;30;45m',  # 5 roxo
    '\033[0;30;46m',  # 6 anis
    '\033[0;30;47m',  # 7 cinza
    '\033[7m'  # 8 branco
)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor])
    print("~" * tam)
    print(f'  {msg}')
    print("~" * tam, end="")
    print(cores[0])
    sleep(1)


def ajuda(com, cor=0):
    titulo(f"Analisando a funcão \'{n}\'", 4)
    print(cores[5])
    help(com)
    print(cores[0])
    sleep(1)


# Programa Principal
while True:
    titulo("SISTEMA DE AJUDA Pyhelp", 2)
    n = input("Digite um método ou funcão: ")
    if n.lower().strip() == "fim":
        break
    else:
        ajuda(n)
titulo("Volte logo", 3)
