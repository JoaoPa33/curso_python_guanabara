from time import sleep


def maior(* valores):
    print("Analizando valores...", flush=True)
    sleep(0.5)
    for c in valores:
        print(c,end=" ", flush=True)
        sleep(0.5)
    print(f"\nForam informados {len(valores)} ao todo")
    if len(valores) == 0:
        print("O maior valor foi 0")
    else:
        print(f"O maior valor foi {sorted(valores)[-1]}")
    print("=-=" * 20)


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# valores = []
# while True:    
#     while True:
#         try:
#             n = int(input("Digite um valor: "))
#             break
#         except ValueError:
#             print("Erro. Digite um número.")
#     valores.append(n)
#     #print(valores)
#     # print(valores)
#     while True:
#         continuar = input("Deseja inserir outro número? [S/N]").upper().strip()[0]
#         if continuar in "SN":
#             break
#         print("Erro. Responda S ou N")    
#     if continuar in "N":
#         break
#     ''''ask = " "
#     while ask not in "SN":
#         ask = input("Deseja adicionar um novo número: [S/N]").upper().strip()[0]
#     if ask == "N":
#         break'''
# print("Analizando valores passados...")
# for c in valores:
#     print (c, end=" ")
# print(f"Foram informados {len(valores)} valores ao todo")
# valores.sort()
# print(f"O maior valor informado foi {valores[-1]}")