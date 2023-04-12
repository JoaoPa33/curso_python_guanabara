#Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

menu = True
#menu = 0
while menu == True:
#while menu != "5":
    print('''ESCOLHA A OPÇÃO QUE DESEJA
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa ''')
    opcao = input("Qual a opção: ")
    if opcao == "1":
        print("A soma entre {} + {} é {}".format(n1, n2, n1 + n2))
    elif opcao == "2":
        print("A multiplicação entre {} x {} é igual a {}".format(n1, n2, n1 * n2))
    elif opcao == "3":
        if n1 > n2:
            print("O número {} é maior que {}".format(n1, n2))
        elif n1 < n2:
            print("O número {} é menor que {}.".format(n1, n2))
        else:
            print("Os números são iguais")
    elif opcao == "4":
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
    elif opcao == "5":
        print("Finalizando...")
        sleep(1)
        menu = False
    else:
        print("Opção inválida. tente novamente.")
    print("=-=" * 20)
print("Fim do program! Volte sempre!")



