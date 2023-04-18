expre =(input("Digite uma expressão: "))
pilha = []
for simb in expre:
    if simb =="(":
        pilha.append("(")
    else:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append("(")
            break
if len(pilha) == 0:
    print("A operaçao esta certa")
else:
    print("Esta faltando parenteses")