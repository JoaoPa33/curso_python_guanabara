from random import randint
from time import sleep
def jogar():
    print("{:=^40}".format("Jogo da Adivinhaçao"))
    print('''Qual nível vc gostaria de selecionar?
    [1] Facil [2]Médio [3]Difícil''')
    nivel = input("Selecine o nível: ")
    if nivel == "1":
        tentativas = 20
    elif nivel == "2":
        tentativas = 10
    elif nivel == "3":
        tentativas = 5
    n_pc = randint(1, 100)
    #print("numero pc {}".format(n_pc))
    c = 1
    pontos = 500
    while c <= tentativas:
        print("Tentativa {} de {}".format(c, tentativas))
        c += 1
        n = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou:{}".format(n))
        print("Processando...")
        sleep(1)
        pontos -= abs(n_pc - n)
        if n > n_pc:
            print("Você errou: O número é MENOR")
        elif n < n_pc:
            print("Você errou: O número é MAIOR")
        elif n == n_pc:
            print("PARABENS você acertou. Você fez {} pontos".format(pontos))
            break
    while c > tentativas:
        print("Você perdeu. O número era {}".format(n_pc))
        break
    print("FIM DE JOGO")
    d = 1
    while d == 1: 
        print("Deseja continuar?")
        continuar = int(input("[1] Sim [2]Não"))
        if continuar == 1:
            jogar()
        elif continuar == 2:
            print("Até a proxima")
            d = 2
        else:
            print("Valor incorreto")
    print("FIM DE JOGO")
if (__name__ == "__main__"):
    jogar()  
