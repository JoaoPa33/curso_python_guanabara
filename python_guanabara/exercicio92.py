from datetime import date
data_atual =2017 #date.today().year
cadastro = {}
while True:
    cadastro["nome"] = input("Nome:")
    while True:
        try:
            nasc = int(input("Ano de nascimento:"))
            break
        except ValueError:
            print("Dado inválido. Tente um número inteiro")
    cadastro["idade"] = data_atual - nasc
    while True:
        try:
            cadastro["clt"] = int(input("Número da carteira de Trabalho (0 se não tem):"))
            break
        except ValueError:
            print("Dado inválido. Tente um número inteiro")
    if cadastro["clt"] == 0:
        break
    while True:
        try:
            cadastro["contratação"] = int(input("Ano de contratação:"))
            break
        except ValueError:
            print("Dado inválido. Tente um número inteiro")
    while True:
        try:
            cadastro["salário"] = float(input("Salário: R$"))
            break
        except ValueError:
            print("Dado inválido. Tente um número inteiro")
    tempo_contribuicao = 35
    ano_aposentadoria = cadastro["contratação"] + 35
    cadastro["aposentadoria"] = ano_aposentadoria - data_atual + cadastro["idade"]
    break
for k, v in cadastro.items():
    print(f"- {k} tem valor {v}")

print(cadastro)