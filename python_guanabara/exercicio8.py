distancia = float(input("Uma distância em metros: "))
print("A distancia de {} coresponda a:\n{:>10}km\n{:>10.0f}cm\n{:>10.0f}mm".format(distancia, distancia/1000, distancia*100, distancia*1000))