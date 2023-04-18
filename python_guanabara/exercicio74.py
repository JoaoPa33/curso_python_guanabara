from random import randint
maior = menor = 0
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f"A lista sorteada foi:", end=" ")
    # print(f"A lista sorteada foi: {numeros}")
for n in numeros:
    print(n, end=" ")
print(f"\nO maior número foi {max(numeros)}")
print(f"O menor numero foi {min(numeros)}")
# lista = ""
# for c in range(0, 5):
#     n = randint(0, 10)
#     if c == 0:
#         maior = menor = n
#     else:
#         if n > maior:
#          maior = n
#     if n < menor:
#         menor = n
#     lista += str(n)

# print(f"O maior número foi {maior}")
# print(f"O menor numero foi {menor}")