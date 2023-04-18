matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0
soma_terceira = 0
maior_seg = 0
for l in range (0, 3):
    for c in range(0, 3):
        while True:
            try:
                valor =(int(input(f"Digite o valor para [{l}, {c}]")))
                break
            except ValueError:
                print("Valor não reconhecido.Tente novamente")
        matriz[l][c] = valor
        if valor % 2 == 0:
            soma_pares += valor

for l in range(0, 3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()    
print("=-=" * 20)
print(f"A soma dos valores pares {soma_pares}")
#matriz[0][2] + matriz[1][2] + matriz[2][2]
for c in range(0,3):
    soma_terceira += matriz[c][2]
print(f"A soma dos valores da terceira coluna é {soma_terceira}")
for l in range(0,3):
    if matriz[1][l] == matriz[1][0]:
        maior_seg = matriz[1][0]
    else:
        if matriz[1][l] > maior_seg:
            maior_seg = matriz[1][l]
print(f"O maior valor da segunda coluna é: {maior_seg}")