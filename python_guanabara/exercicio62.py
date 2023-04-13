n = float(input("Qual o primeiro termo:"))
r = float(input("Qual a razão: "))
cont = 1
amais = 10
total = 0
while amais != 0:
    total += amais
    while cont <= total:
        print("{} -".format(n), end=" ")
        n += r
        cont += 1
    print("PAUSA")
    amais = int(input("Quantos termos vc quer mostrar a mais:"))
print("Progressao finalizada com {} termos mostrados".format(total))
