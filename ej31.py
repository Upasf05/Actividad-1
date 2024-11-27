import math
def areacirc(radio):
       return math.pi * radio ** 2
print("Ingrese el radio del círculo a calcular: ")
radio = float(input())
resultado = areacirc(radio)
print("El área es: " + str(round(resultado, 2)))
