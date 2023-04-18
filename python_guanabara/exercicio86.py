modulo = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        while True:
            try:
                modulo[l][c] = (int(input(f"Digite um valor para [{l},{c}]: ")))
                break
            except ValueError:
                print("Valor incorreto. Tente novamente")
for l in range(0, 3):
    for c in range(0,3):
        print(f"[{modulo[l][c]:^5}]", end=" ")
    print()
# modulo = [[],[],[]]
# for x in range(0,3): 
#     for y in range(0,3):
#         while True:
#             try:
#                 modulo[x].append(int(input(f"Digite um valor para [{x},{y}]: ")))
#                 break
#             except ValueError:
#                 print("Valor incorreto. Tente novamente")
# print("=-=" * 20)
# for x in range(0,3):
#     conta = 0
#     for y in range(0,3):
#         print(f"[{modulo[x][y]:^5}]", end=" ")
#         conta += 1
#     if conta == 3:
#         print("\n")
      
# print(f"\n{modulo}")

