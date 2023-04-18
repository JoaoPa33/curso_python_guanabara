tupla = ("Aprender", "Programar", "Linguagem","Python")
for p in tupla:
    print(f"\nA palavra {p.upper()} tem as vogais :", end="")
    for letra in p:
        if letra.upper() in "AEIOU":
            print(letra.upper(), end=" ")

