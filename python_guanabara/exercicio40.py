n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2
if media < 5:
    status = "\033[31mREPROVADO\033[37m"
elif 5 <= media < 7:
    status = "\033[34mRECUPERAÇÃO\033[37m"
else:
    status = "\033[32mAPROVADO\033[37m"
print("O aluno está {} e sua média é de {:.1f}.".format(status, media))