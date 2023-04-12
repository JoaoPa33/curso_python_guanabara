import math
# or from math import hypot

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))

print("A hipotenusa vai medir {:.2f}".format(math.hypot(oposto, adjacente)))