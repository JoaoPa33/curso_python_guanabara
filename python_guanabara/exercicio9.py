n = int(input("Digite um número da tabuada: "))
multiplo = 0
print("=" * 12)
while(multiplo <= 10):
     print("{:2} x {:2} = {}".format(n, multiplo, (n * multiplo)))
     multiplo += 1
print("=" * 12)

for multiplo in range(0,11):
    print("{:2} x {:2} = {}".format(n, multiplo, (n * multiplo)))
print("=" * 12)