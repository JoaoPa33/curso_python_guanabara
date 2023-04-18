print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)
produtos = ("lapis", 1.75, "borracha", 2)
for p in range(0,len(produtos)):
    if p % 2 == 0:
        print(f"{produtos[p] :.<30}", end="")
    else:
        print(f"R${produtos[p]:>8.2f}")
print("-" * 40)

    