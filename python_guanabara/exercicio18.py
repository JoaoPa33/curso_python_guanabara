from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que vc deseja: "))
radianos = radians(angulo)
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, sin(radianos)))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cos(radianos)))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(angulo, tan(radianos)))

