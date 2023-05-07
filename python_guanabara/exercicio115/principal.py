from libry.interacao import *
from libry.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)
# if arquivoExiste(arq): # se retornar True da função 
#     print('Arquivo encontrado')
# else:#se retornar Falso da funçao
#     print('Arquivo não encontrado')
#     criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar novas pessoas", "Sair do sistema"])
    if resposta in [1,2]:
        cabecalho("Opção", resposta)
        if resposta == 1:
            lerArquivo(arq)
        elif resposta == 2:
            cabecalho("Adicionando nova pessoa")
            nome = input("Nome: ").capitalize()
            idade = leiaInt("Idade: ", "")
            cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho("Fim do Sistema. Até logo")
        break
    else:
        print(f"\033[31mErro: valor inválido\033[m")
    sleep(1)
    
