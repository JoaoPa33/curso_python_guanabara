def ficha(j = "<desconhecido>", g = 0):
    return f"O jogador {j} fez {g} no campeonato."


a = input("Digite o nome de um jogador: ")
gols = input("Quantos gols ele fez:")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if a.strip() == "":
    print(ficha(g = gols))
else:
    print(ficha(a, gols))

    
# lista_de_atletas = [{"nome":"Gabriel", "gols": 3},
#                     {"nome":"Pedro", "gols": 6},
#                     {"nome":"Cebola", "gols":1},
#                     {"nome":"Marinho", "gols":0},]
# while True:
#     try:
#         jogador = input("Digite o nome de um jogador: ").strip().capitalize()
#         if any(c["nome"] == jogador for c in lista_de_atletas):
#         # se qualquer(xx["nome"] == a para xx in lista)
#             break
#     except ValueError:
#         print("Erro digite um nome válido")


        