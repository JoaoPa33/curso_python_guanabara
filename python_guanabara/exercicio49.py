print("\033[34m=-=\033[37m" * 20)
valor = int(input("Digite um número da tabuada:"))
for tabuada in range (0, 11):
    print("{:2d} x {:2d} = {:<3d}".format(valor, tabuada, valor * tabuada))
print("\033[34m=-=\033[37m" * 20)
