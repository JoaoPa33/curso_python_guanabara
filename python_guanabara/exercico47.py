#otimizado(exige menos laços)
for contagem in range (2, 51, 2):
    print(contagem, end=" ")
print("Acabou")

#consome mais processador pq repete mais vezes o laço
for contagem in range (1, 51):
    if contagem % 2 == 0:
        print(contagem, end=" ")
print("Acabou")
