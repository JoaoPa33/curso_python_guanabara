from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0, 5):
        valor = randint(0, 10)
        lista.append(valor)
    print(f"Foram sorteados 5 valores:", end=" ")
    for v in lista:
        print(v, end= " ",flush=True)
        sleep(0.5)
    print(f"PRONTO")


def somaPar(lista):
    soma = 0
    for x in numero:
        if x % 2 == 0:
            soma += x
            
    print(f"Somando os valores pares de {lista}, temos {soma}")

    
numero = []
sorteia(numero)
somaPar(numero)

