from datetime import date
data = int(input("Que ano quer analisar? Coloque 0 para analizar o ano atual: "))
if data == 0:
    data = date.today().year
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print("O ano {} é \033[34m Bissexto\033[37m".format(data))
else:
        print("O ano {} é \033[34m NÃO é Bissexto\033[37m".format(data))
    