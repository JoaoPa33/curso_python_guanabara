#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = c = 0
posicao = 1
while True:
    n = int(input("Digite um número inteiro [999 para sair]:"))
    if n == 999:
        break
    else:
        if c == 0:
            menor = maior = n
            maior_posicao = menor_posicao = 1
        else:
            if n > maior:
                maior = n
                maior_posicao = posicao
            elif n < menor:
                menor = n
                menor_posicao = posicao
        c += 1
        soma += n
        posicao += 1
print(f"Foram digitados {c} e a soma foi {soma}")
print(f"O maior foi {maior} e foi o {maior_posicao} elemento, o menor foi {menor} e foi o {menor_posicao} elemento.")