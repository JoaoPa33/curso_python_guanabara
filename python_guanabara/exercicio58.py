#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint
from time import sleep

numero = randint(0, 10)
#print(numero)
print("Sou seu computador.. Acabei de pensar em um número dentre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpite = 0
while not acertou:
    palpite += 1
    #print("{} palpite".format(palpite))
    jogador = int(input("Digite um valor:"))
    print("Processando...")
    sleep(1)
    if jogador == numero:
        acertou = True
    else:
        if jogador > numero:
            print("Menos...")
        elif jogador < numero:
            print("Mais ....")
print("Parabens vc acertou em {} tentativas".format(palpite))



#ou
numero = randint(0, 10)
#print(numero)
print("\033[34m=-="*20)
print("\033[37mVou pensar em um número entre 0 e 10.Tente adivinhar...")
print("\033[34m=-=\033[m"*20)
chute = int(input("Em que número eu pensei? :"))
palpite = 1
while chute != numero:
    print("Processando....")
    sleep(1)
    #print("{} de tentativas".format(palpite))
    print("\033[1;31mVocê errou\033[m")
    palpite += 1
    if chute > numero:
        print("O numero que pensei é menor")
    else:
        print("O numero que pensei é maior")
    print("=-=" * 40)
    chute = int(input("Digite um número:"))
print("Processando....")
sleep(1)
print("\033[1;32mParabens\033[m você acertou o número é {} e vc utilizou {} tentativas".format(numero, palpite))
