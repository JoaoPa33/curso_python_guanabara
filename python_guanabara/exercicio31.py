dist = int(input("Qual a distância de sua viagem?"))
if(dist <= 200):
    print("Sua viagem custará R${:.2f}.".format(dist * 0.5))
else:
        print("Sua viagem custará R${:.2f}.".format(dist * 0.45))
#OU

dist = int(input("Qual a distância de sua viagem?"))
if(dist <= 200):
    preço = dist * 0.5
else:
    preço = dist * 0.45
print("Sua viagem custará R${:.2f}.".format(preço))

#OU
dist = int(input("Qual a distância de sua viagem?"))
preço = dist * 0.5 if dist <= 200 else dist * 0.45
print("Sua viagem custará R${:.2f}.".format(preço))
