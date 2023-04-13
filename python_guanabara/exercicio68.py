#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print("=-"*40)
print("Vamos jogar PAR ou IMPAR")
print("=-"*40)
vitoria = 0
while True:
    print("=-"*40)
    pc = randint(0, 10)
    #print(f"numero do pc {pc}")
    num = int(input("Digite um valor: "))
    total = pc + num
    opcao = " "
    while opcao not in "pi":
        opcao = input("Par ou Impar? [P/I]:").strip().lower()[0]
    if opcao in "p":
        if total % 2 == 0:
            print(f"Você jogou {num} e o computador {pc}. Total de {total} deu PAR")
            print("\033[1;32mVoce ganhou\033[m")
            vitoria += 1  
        else:
            print(f"Você jogou {num} e o computador {pc}. Total de {total} deu IMPAR")
            print("\033[1;31mVoce perdeu\033[m")
            break
    elif opcao in "i":
        if total % 2 != 0:
            print(f"Você jogou {num} e o computador {pc}. Total de {total} deu IMPAR")
            print("\033[1;32mVoce ganhou\033[m")
            vitoria += 1  
        else:
            print(f"Você jogou {num} e o computador {pc}. Total de {num + pc} deu PAR")
            print("\033[1;31mVoce perdeu\033[m")
            break
print(f"GAME OVER! Você venceu {vitoria} vezes.")

