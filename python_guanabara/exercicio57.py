# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Informe seu sexo:[M/F]").strip().upper()[0]
while sexo not in "MF":
    sexo = input("Dados invalidos.Informe seu sexo:[M/F]").strip().upper()[0]    
print("Sexo {} registrado com sucesso".format(sexo))
# ou
sexo = input("Informe seu sexo:[M/F] ").upper()[0]
if (sexo == "M" or sexo == "F"):
    print("Sexo {} registrado com sucesso".format(sexo))
else:
    while (sexo != "M" and sexo != "F"):
        sexo = input("Dados inválidos. Por favor, informe seu sexo:").upper()
    print("Sexo {} registrado com sucesso".format(sexo))
    
#ou
sexo = input("Informe seu sexo:[M/F] ")
if (sexo in "MnFf"): # ele precisa atender apenas uma condicao para ser verdadeiro
    print("Sexo {} registrado com sucesso".format(sexo))
else:
    while (sexo not in "Mm" and sexo not in "Ff"): # ele precisa atender as duas condicoes para ser vedadeiro
        sexo = input("Dados inválidos. Por favor, informe seu sexo:").upper()
    print("Sexo {} registrado com sucesso".format(sexo))
            