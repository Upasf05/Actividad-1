import random
numeroaleatorio = random.randint(1, 10)
print("Adivina el número del 1 al 10")
adivinanza = int(input())
if adivinanza == numeroaleatorio:
      print("¡Acertaste!")
else:
      print("El número era" +numeroaleatorio+ ", pero has estado cerca")
