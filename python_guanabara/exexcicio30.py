n = int(input("Me diga um número inteiro:"))
resultado = n % 2
if(resultado == 0):
    print("O número {} é \033[34mPAR\033[37m".format(n))
else:
    print("O número {} é \033[34mIMPAR\033[37m".format(n))