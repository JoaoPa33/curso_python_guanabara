# numeros primos são divisiveis por 1 e  por ele mesmo
valor = int(input("Digite um número: "))
total = 0
for c in range(1, valor + 1):
    if valor % c == 0:
        print("\033[1;31m{}\033[m".format(c), end=" ")
        total += 1
    else:
        print("{}".format(c), end=" ")
print("\nO número: {} foi divisivel {} vezes".format(valor, total))
if total == 2:
    print("E por isso ele é primo")
else:
    print("Ele não é primo")
    
# ou
valor = int(input("Digite um número: "))
total = 0
alt = 1
for c in range(alt, valor + 1):
    if valor % c == 0:
        print("\033[1;31m{}\033[m".format(c), end=" ")
        total += 1
    else:
        print("{}".format(c), end=" ")
    alt += 1
print("\nO número: {} foi divisivel {} vezes".format(valor, total))
if total == 2:
    print("E por isso ele é primo")
else:
    print("Ele não é primo")
    