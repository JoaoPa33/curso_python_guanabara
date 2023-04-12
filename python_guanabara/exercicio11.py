lar = float(input("Largura da parede:"))
alt = float(input("Altura da parede:"))

area = lar * alt 
rendimento_da_tinta = area / 2

print(f"Sua parede tem a dimenção de {lar}x{alt} e sua área é de {(area):.3f}m.\nPar pintar essa parede, você precisará de {rendimento_da_tinta}l de tinta.")