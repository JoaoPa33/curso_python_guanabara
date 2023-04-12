a = int(input("\033[031mDigite o primeiro número:"))
b = int(input("\033[032mDigite o segundo número:"))
c = int(input("\033[033mDigite o terceiro número:"))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"\033[037mO menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")