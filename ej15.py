print("Sistema estadounidense de exámenes")
print("Ingrese un número del 0 al 100 para obtener una nota de examen de la A a la F")
nota = int(input())
if 90 >= nota >= 100:
      letra= "A, excelente"
elif 80 >= nota >= 89:
      letra= "B, satisfactorio"
elif 60 >= nota >= 79:
      letra= "C, aceptable"
elif 40 >= nota >= 59:
      letra= "D, mejorable"
else:
      letra = "F, reprobado"
