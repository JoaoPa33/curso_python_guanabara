from ..interacao import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt") #rt = reed e text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, "wt+")  
    except:
        print("Houve um erro ao criar o arquivo!") 
    else:
        print(f"Arquivo {nome} criado com sucesso")
    # finally:
        # a.close()


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro: ao ler o arquivo')
    else:
        cabecalho("Pessoas Cadastradas")
        #print(a.read()) #pode ser readlines ou read só tambem
        #return linhas
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
             #print(f'{dado[0]}{dado[1]}')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at') # "r" ler "w" escrever "+" criar arquivo "a" acrescentar
    except:
        print("Houve um Erro na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um erro na hora de escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado.")  
            a.close()



