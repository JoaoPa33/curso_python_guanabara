def leiaInt(msg):
    valor = 0
    #ok = False
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = float(n)
            break
        else:
            print("Erro. digite um número valido")
        #if ok:
        #   break
    return valor


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")