#Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
n = int(input("Digite um número: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n, f))

#ou

n = int(input("Digite um número: "))
print("Calculando fatorial de {}! =".format(n), end="")
fatorial = 1
for c in range(n, 0, -1):
    fatorial *= c
    if c == 1:
        print(" 1 = {}".format(fatorial))
    else:
        print(" {} x".format(c), end="")

#ou

fatorial = 1
while n != 0:
#while c > 0
    fatorial *= n
    if n != 1:
        print("{}".format(n), end = " x ")
    else:
        print("1 = {}".format(fatorial))
    #print("{}".format(c))
    # print("x" if c > 1 else "=", end=" ") 
    #print(fatorial)
    n -= 1
    
