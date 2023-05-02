def escreva (text):
    print("~" * (len(text) + 4))
    print(f'  {text}')
    print("~" * (len(text) + 4))


# Programa principal
while True:
    titulo = input("Digite um texto:[000 para sair]")
    if titulo == "000":
        break
    escreva(titulo)
