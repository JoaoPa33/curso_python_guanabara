nome = str(input("Digite seu nome completo: ")).strip()

list_nome = nome.split()
join_nome = "".join(list_nome)

print("Analisando seu nome...")
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print(f"Seu nome em letras minusculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(join_nome)} letras")
print(f"Seu primeiro nome é {list_nome[0]} e ele tem {len(list_nome[0])} letras")

#guanabara
print("Analisando seu nome...")
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print(f"Seu nome em letras minusculas é {nome.lower()}")
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome é {} e ele tem {} letras".format(list_nome[0], nome.find(" ")))
