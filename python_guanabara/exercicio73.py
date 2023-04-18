times = ("Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR", "São Paulo", "Internacional", "Corinthians", "Fortaleza", "Goiás", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Botafogo", "Ceará", "Cruzeiro", "CSA", "Chapecoense", "Avaí")
print("=-=" * 15)

print("A) Os 5 primeiros são:")
for t in range(0,5):
    print(times[t])
print(f"A) Os 5 primeiros são:{times[0:5]}")

print("=-=" * 15)

print("B) Os 4 ultimos são:") #[-1:-5:-1]
for t in range(16, len(times)):
    print(times[t])
print(f"B) Os 4 ultimos são: {times[16:]}") #[-1:-5:-1] [-4:]

print("=-=" * 15)

print("C) A lista em ordem alfabetica é:")
times_alf = sorted(times)
for t in range(0, len(times)):
    print(times_alf[t])
print(f"C) A lista em ordem alfabetica é: {sorted(times)} ")

print("=-=" * 15)

print("D) Qual a posição da Chapecoense? {}".format(times.index("Chapecoense")+ 1))
