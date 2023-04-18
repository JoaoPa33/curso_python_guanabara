turma = []
media = []
aluno = []
while True:    
    nome = input("Nome:")
    aluno.append(nome)
    while True:
        try:
            nota1 = float(input("Nota 1:"))
            break
        except ValueError:
            print("Valor não aceito. Tente novamente")
    aluno.append(nota1)
    while True:
        try:
            nota2 = float(input("Nota 2:"))
            break
        except ValueError:
            print("Valor não aceito. Tente novamente")
    aluno.append(nota2)
    med = (nota1 + nota2) / 2
    media.append(med)
    aluno.append(media[:])
    turma.append(aluno[:])
    media.clear()
    aluno.clear()

    
    cont = " "
    while cont not in "SN":
        cont = input("Quer continuar?[S/N]").upper().strip()[0]   
    if cont == "N":
        break 
print("=-=" * 30)
print("No. NOME          MÉDIA")
for i, l in enumerate(turma):
    print(f"{i:<4}{l[0]:<14}{l[3]}")
while True:
    opc = int(input("Mostrar a nota de qual aluno? (999 interrompe)"))
    if opc == 999:
        break
    if opc <= len(turma) - 1:
        print(f"Notas de {turma [opc][0]} são {turma[opc][1]} {turma[opc][2]} ")



#print(turma)
