from random import randint
from time import sleep

print("{:=^40}".format("\033[34mJOGO JOKENPO\033[37m"))

itens = ["", "Pedra", "Papel", "Tesoura"]
computador = randint(1, 3) #poderia colocar aparetir do 0 mas ai teria que trocar o item pedra para zero
print('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input("Qual é a sua jogada?: "))
print("JO")
sleep(1)
print("Ken")
sleep(1)
print("PO")
print("=-=" * 20)
if jogador == 1 or jogador == 2 or jogador == 3:
    if jogador == computador:
        print("\033[1;33mEMPATE\033[0;37m")
        print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
    elif computador == 1:#PEDRA
        if jogador == 2: #vitoria
            print("\033[1;32mVITÓRIA\033[0;37m")
            print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
        elif jogador == 3: #derrota
            print("\033[1;31mDERROTA\033[0;37m")
            print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
    elif computador == 2:#PAPEL
        if jogador == 3: #vitoria
            print("\033[1;32mVITÓRIA\033[0;37m")
            print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
        elif jogador == 1: #derrota
            print("\033[1;31mDERROTA\033[0;37m")
            print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
    elif computador == 3:#TESOURA
        if jogador == 1: #vitoria
            print("\033[1;32mVITÓRIA\033[0;37m")
            print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
        elif jogador == 2: #derrota
            print("\033[1;31mDERROTA\033[0;37m")
            print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))


else:
    print("Jogada \033[1;31minvalida\033[0;37m.")
print("{:=^40}".format("\033[31mFIM DE JOGO\033[37m"))

# print("{:=^40}".format("\033[34mJOGO JOKENPO\033[37m"))
# print('''Escolha um um número:
# [1] Pedra
# [2] Papel
# [3] Tesoura''')
# me = int(input("Escolha um:"))
# #gerando opcao do pc
# numero_pc = randint(1,3)
# if numero_pc == 1:
#     pc = "Pedra"
# elif numero_pc == 2:
#     pc = "Papel"
# elif numero_pc == 3:
#     pc = "Tesoura"

# if me == 1:
#     me_opcao = "Pedra"
# elif me == 2:
#     me_opcao = "Papel"
# elif me == 3:
#     me_opcao = "Tesoura"

# if me == 1 or me == 2 or me == 3:
#     print("JO")
#     sleep(1)
#     print("KEN")
#     sleep(1)
#     print("PO")
#     if me == 1 and numero_pc == 3 or me == 2 and numero_pc == 1 or me == 3 and numero_pc == 2:        
#         print('''Você \033[32mGANHOU\033[37m:
# O PC escolheu {}
# Você escolheu {}
# {:=^40}'''.format(pc, me_opcao, "\033[31mFIM DE JOGO\033[37m"))
#     elif me == 1 and numero_pc == 2 or me == 2 and numero_pc == 3 or me == 3 and numero_pc == 1:
#         print('''Você \033[31mPERDEU\033[37m:
# O PC escolheu {}
# Você escolheu {}
# {:=^40}'''.format(pc, me_opcao, "\033[31mFIM DE JOGO\033[37m"))
#     else:
#         print('''Vocês empataram:
# O PC escolheu {}
# Você escolheu {}
# {:=^40}'''.format(pc, me_opcao, "\033[31mFIM DE JOGO\033[37m"))
    
# else:
#     print("Você não escolheu uma opção válida\n{:=^40}".format("\033[31mFIM DE JOGO\033[37m"))
