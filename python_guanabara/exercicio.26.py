n = input("Digite uma frase: ").strip()
print("A letra A aparece {} vezes na frase".format(n.upper().count("A")))
print("A primeira letra A apareceu na posiçao {}".format(n.upper().find("A") + 1))
print("A ultima letra A apareceu na posicao {}".format(n.upper().rfind("A") + 1))