from random import randint
from time import sleep
from operator import itemgetter
dic = {"jogador1": randint(1,6), "jogador2": randint(1,6), "jogador3": randint(1,6), "jogador4": randint(1,6)}
organizado = []
print("Valor sorteado")
for k, v in dic.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
print("=-=" * 10)
print(f"{'RANKING DOS JOGADORES':=^30}")
organizado = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(organizado)
for i , v in enumerate(organizado):
    print(f"{i + 1}° lugar: {v[0]} com {v[1]}")