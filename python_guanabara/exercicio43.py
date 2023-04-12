print("=-=" * 20)
print("\033[1;031mAnalizando o IMC\033[0;037m")
print("=-=" * 20)
weight = float(input("Qual o peso? (Kg)"))
height = float(input("Qual a sua altura? (m)"))
imc = weight / pow(height, 2)
if imc < 18.5:
    status = "\033[31mAbaixo do peso\033[37m" 
elif 18.5 <= imc < 25:
    status = "\033[31mPeso ideal\033[37m"
elif 25 <= imc < 30:
    status = "\033[31mSobre peso\033[37m"
elif 30 <= imc <= 40:
    status = "\033[31mObesidade\033[37m"
else:
    status = "\033[31mObesidade Morbida\033[37m"
print("Seu IMC é de {:.1f}, logo você esta com {}.".format(imc, status))
