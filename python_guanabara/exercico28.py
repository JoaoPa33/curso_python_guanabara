from random import randint
from time import sleep

numero = randint(0, 5)
print(numero)
print("\033[34m=-="*20)
print("\033[37mVou pensar em um número entre 0 e 5.Tente adivinhar...")
print("\033[34m=-=\033[m"*20)
chute = int(input("Em que número eu pensei? :"))
print("Processando....")
sleep(2)
if (numero == chute):
    print("\033[32mPARABENS você acertou o numero que pensei foi {}".format(chute))
else:
    print("\033[31mVocê errou, eu pensei no número {}!".format(numero))
