#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = contador = c = 0
n = int(input("Digite um numero: "))
while n != 999:
    c += 1
    contador += n
    n = int(input("Digite um numero: "))
print("Você digitou {} numeros e a soma entre elees foi {}".format(c, contador))



