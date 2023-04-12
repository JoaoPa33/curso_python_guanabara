from datetime import date
data_atual = 2017#date.today().year
maiores = 0
menores = 0
for dat in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu?".format(dat)))
    if data_atual - nasc >= 18:
        maiores += 1
    else:
        menores += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E tambem tivemos {} menores de idade.'''.format(maiores, menores))
