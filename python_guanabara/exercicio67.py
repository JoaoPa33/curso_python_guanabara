#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print("-" * 40)
    n = int(input("Quer ver a tabuada de qual número?: "))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f"{n} X {c:2} = {n * c}")
print("FIM")   
    
