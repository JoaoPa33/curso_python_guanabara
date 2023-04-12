primeiro = int(input("Digite o primeiro valor:"))
segundo = int(input("Digite o segundo valor:"))

maior = "primeiro"

if primeiro < segundo:
    maior = "segundo"
elif primeiro == segundo:
    print("Não existe valor maior, os dois são iguais")
print(f"O {maior} valor é o maior")