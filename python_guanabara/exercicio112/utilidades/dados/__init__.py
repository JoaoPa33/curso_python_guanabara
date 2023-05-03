def leia_dinheiro(n):
    # valido = False
    # while not valido:
    #     valor= input(f"{n}").replace(',','.').strip()
    #     if valor.isalpha() or valor == '':
    #         print(f"\033[31mErro \'{valor}\' é um preço inválido\033[m.")
    #     else:
    #         valor = float(valor)
    #         valido = True
    # return valor  


#Minha soluçao
    while True:
        valor = input(f'{n}').replace(',', ".").strip()    
        try:
            valor = float(valor)
            break
        except ValueError:
              print(f"\033[31mErro \'{valor}\' é um preço inválido\033[m.")
    return valor          