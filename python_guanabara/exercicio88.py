from random  import randint
from time import sleep
print("=-" * 30)
print(f"{'JOGA MEGA SENA':^30}")
print("=-" * 30)
while True:
    try:
        valor = int(input("Quantos jogos você quer que eu sortei? "))
        break
    except ValueError:
        print("Valor não aceito tente novamente.")
print(f"{' SORTEANDO JOGOS ':=^30}")
for c in range(1, valor + 1):
    cont=0
    jogo = []
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    print(f"O jogo {c} é: {jogo}")
# NO CASO DE BAIXO SERA CRIADO UMA LISTA DENTRO DE UMA LISTA

# jogo = []
# lista =[]
# quant = int(input("Quantos jogos você quer que eu sorteie? "))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont == 6:
#             break
#     lista.sort()
#     jogo.append(lista[:])
#     lista.clear()
# for i, l in enumerate(jogo):
#     print(f"Jogo {i+1}: {l}")
#     sleep(1)
    
