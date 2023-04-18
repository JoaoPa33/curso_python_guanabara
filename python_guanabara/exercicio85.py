temp = []
numeros = [[], []]

for c in range(1,8):
    while True:
        try:
            n = int(input(f"Digite o {c} valor: "))
            break
        except ValueError:
            print("Valor invalido. Tente novamente")
    if n % 2 == 0:
        numeros[0].append(n)
    elif n % 2 == 1:
        numeros[1].append(n)
print(numeros)
numeros[0].sort()
numeros[1].sort()

print(f"Os numeros pares foram:")# {numeros[0]}")
filtro = []
for c in numeros[0]:
    if c not in filtro:
        filtro.append(c)
        print(c, end=" ")
del filtro[0:]     
print(f"\nOs números impares foram:")# {numeros[1]}")
for c in numeros[1]:
    if c not in filtro:
        filtro.append(c)
        print(c, end=" ")
