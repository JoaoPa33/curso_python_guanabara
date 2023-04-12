import emoji
print("==" * 20)
print("{:^40}".format("10 TERMOS DE UMA PA"))
print("==" * 20)
termo1 = float(input("Primeiro termo:"))
razao = float(input("Razão:"))
for c in range (0, 10):
    print(emoji.emojize("{:.0f} :right_arrow: ".format(termo1)), end=" ")
    termo1 += razao
print("ACABOU") 