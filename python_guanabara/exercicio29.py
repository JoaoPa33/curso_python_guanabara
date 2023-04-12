import time

speed = float(input("Qual a velocidade atual de um carro? :"))
velocidade_limite = 80
multa = (speed - velocidade_limite) * 7
print("Analisando...")
time.sleep(2)
if (84 >= speed > 80):
    print("\033[33mVocê esta acima da velocidade permitida\nMas temos a tolerância de  5%. Atenção")
elif (speed > 84):
    print("\033[1;31mMULTADO!\033[0;31m Você excedeu o limite permitido que é de 80 km/h \nVocê deve pagar uma multa de \033[33mR${:.2f}\033[31m.".format(multa))
print("\033[32mTenha um bom dia! Dirija com segurança!\033[m")
    