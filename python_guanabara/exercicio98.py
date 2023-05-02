from time import sleep

def contador (inicio, fim, passo):
    print("=-=" * 20)
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}")
    if inicio > fim:
        passo = -abs(passo)
        for c in range(inicio, fim - 1, passo):
            sleep(0.5)
            print(c, end=" ", flush=True)
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(c, end=" ", flush=True)
    print(f"FIM")
    

# PROGRAMA PRINCIPAL
contador (1, 10, 1)
contador (10, 0, 2)

print("=-=" * 20)
print("Agora é sua vez de personalizar a contagem:")
a = int(input("Inicio:"))
b = int(input("Fim:"))
c = int(input("Passo:"))

contador(a, b, c)