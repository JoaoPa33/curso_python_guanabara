dic = {}
dic["nome"] = input("Nome:")
while True:
    try:
        dic["media"] = float(input(f"Média de {dic['nome']}:"))
        break
    except ValueError:
        print("Valor não aceito. Tente novamente") 

while dic["media"] > 10:
        print("Valor não aceito")
        dic["media"] = float(input(f"Média de {dic['nome']}:"))     
        
if 10>=dic["media"] >= 7:
    dic["status"] = "Aprovado"
elif 5 <=dic["media"] < 7:
    dic["status"] = "Recuperação"
else:
    dic["status"] = "Reprovado"
print("=-" * 30)
for k, v in dic.items():
    print(f"O {k} é igual {v}")
# print(f"Nome é igual a {dic['nome']}")
# print(f"Média é igual a {dic['media']}")
# print(f"Situação é igual a {dic['status']}")




# dados = {"nome": "Pedro", "idade": 20}
# print(dados)
# print(dados["nome"])
# dados["sexo"] = "m"
# print(dados)
# print(len(dados))
# print(dados.items())
# print(dados["nome"])