from time import sleep
jogador = {}
gols = []
jogador["nome"] = input("Nome do jogador: ")
while True:
    try:
        quantidade_jogos = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
        print("    Processando ....")
        sleep(1)
        break
    except ValueError:
        print("    Processando....")
        sleep(1)
        print("Erro no dado. Tente um número")
#total_gols = 0
for i in range(1,quantidade_jogos + 1):
    while True:
        try:
            gol = int(input(f"Quantos gols na partida {i}: "))
            break
        except ValueError:
            print("Erro. O valor precisa ser um número inteiro")
    #total_gols += gol
    gols.append(gol)
jogador["gol"] = gols[:]
jogador["total_gols"] = sum(gols) #sum realiza uma soma dos itens de uma lista
print("=-=" * 30)
print(f"dicionario {jogador}")
print("=-=" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}") 
print("=-=" * 30)
print(f"O jogador {jogador['nome']} jogou {quantidade_jogos} partidas")# quantidade_jogos = len(jogador["gol"])
for i, v in enumerate(gols):# gol pode ser substituido por (jogador["gol"])
    print(f" -> Na partida {i + 1}, fez {v} gols")
print(f"Foi um total de {jogador['total_gols']} gols.")
