from datetime import date
ano_nasc = int(input("Digite sua data de nascimento:"))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
tempo = abs(18 - idade)
print('''Qual o seu sexo:
[1]Masculino
[2]Feminino''')
sexo = int(input("Qual o sexo?"))
if sexo == 2:
    print("Obrigado. Conte sempre com as Forças Armadas")
else:
    if idade < 18:
        print(f"Ainda não chegou sua hora, você tem {idade}. Aliste-se daqui {tempo} ano(s).\nSeu alistamento será em {ano_nasc + 18}")
    elif idade == 18:
        print("Chegou a sua hora de se alistar. Você ja tem 18 anos")
    else:
        print(f"Ja passou a hora de se alista, você ja tem {idade}. Vc passou do prazo por {tempo} ano(s).\nSeu alistamento deveria ter sido feito em {ano_nasc + 18}")
        if 19 <= idade <= 22:
            #multa de 100 reais por ano
            print("Você tem uma multa pendente de \033[31mR${:.2f}\033[37m.".format((idade - 18) * 100))
        else:
            #multa de 130 reais por ano
            print("Você tem uma multa pendente de \033[31mR${:.2f}\033[37m.".format((idade - 18) * 130))
print("FIM")
                