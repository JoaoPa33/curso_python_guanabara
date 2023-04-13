#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci
termos = int(input("Quantos termos você quer mostrar:"))
c = 3
t1 = 0
t2 = 1
print("{} - {}".format(t1, t2), end=" ")
while c <= 10:
    t3 = t1 + t2
    print("- {}".format(t3), end=" ")
    t1 = t2
    t2 = t3
    c += 1