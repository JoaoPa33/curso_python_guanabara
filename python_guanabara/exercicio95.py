from time import sleep
jogador = {}
gols = []
time = []
while True:
    jogador["nome"]= input("Nome do jogador:").capitalize()
    while True:
        try:
            jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
            break
        except ValueError:
            print("Erro. Digite um valor inteiro.")
    for i in range(1, jogador["partidas"] + 1):
        while True:
            try:
                gol_partida = int(input(f"Quantos gols na partida {i}?"))
                break
            except ValueError:
                print("Erro. Insira um número inteiro.")
        gols.append(gol_partida)
    jogador["gol"] = gols[:]
    jogador["total_gols"] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    #print(time)
    while True:
        continuar = input("Deseja inserir outro jogador? [S/N]").upper().strip()[0]
        if continuar in "SN":
            break
        print("Erro. Responda S ou N")    
    if continuar in "N":
        break
print("=-" * 30)
print(f"{'cod':3} {'nome':<15} {'gols':<15} {'partidas':^8} {'média/partida':^14}")
print("-" * 60)
for i, v in enumerate(time):
     print(f"{i+1:^3} {v['nome']:<15} {str(v['gol']):<15} {v['partidas']:^8} {v['total_gols']/v['partidas']:^.2f}") 
''''   ")
    print(i, v["nome"])
'''
while True:
    while True:
        try:
            dados = int(input("Mostrar dados de qual jogador(cod.)?(999 para sair)"))
            break
        except ValueError:
            print("Erro. valor inválido")
    if dados == 999:
        print("<<<Fim>>>")
        break
    if dados > len(time) or dados == 0:
        print(f"Erro não existe jogador com código {dados}")
    else:
        dados-=1
        print(f"--DADOS DO JOGADOR {time[dados]['nome']} --")
        for i, g in enumerate(time[dados]["gol"]):
            print(f"Na partida {i + 1} ele fez {g} gols")
        
