print("=-=" * 20)
print("\033[1;031mAnalizando um Triangulo\033[0;037m")
print("=-=" * 20)
a = float(input("Primeiro segmento:"))
b = float(input("Segundo segmento:"))
c = float(input("Terceiro segmento:"))
if a + b > c and a < b + c and a + c > b:
    print("Os segmentos acima podem formar um triangulo.", end = " ")
    if a == b == c:
        print("E é EQUILATERO")
    elif a == b or a == c or b == c:
        print("E é ISOSCELES")
    else:
        print("E é ESCALENO")
else:
    print("Os segmentos acima \033[31mNÃO\033[37m podem formar um triangulo")