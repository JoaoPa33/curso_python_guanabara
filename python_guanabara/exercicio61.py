#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
n = float(input("Qual o primeiro termo:"))
r = float(input("Qual a razão: "))
c = 1
while c < 11:
#while c <= 10:
    print(" {} ".format(n), end="-")
    n += r
    c += 1
print(" FIM")

#ou
num = float(input("Qual o primeiro termo:"))
raz = float(input("Qual a razão: "))
for c in range(0, 10):
    print(" {} ".format(num), end="-")
    num += raz
print("FIM")

