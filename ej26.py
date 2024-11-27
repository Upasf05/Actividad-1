import math

def promedio():
       calificaciones = []
       while True:
               print("Inserte sus calificaciones")
               calificacion = float(input())
               if calificacion == 1:
                     break
               calificaciones.append(calificacion)
       if calificaciones:
            prom = math.fsum(calificaciones) / len(calificaciones)
            print("promedio finales:" + str(round(prom, 2)))
       else:
            print("No se ingresaron calificaciones.")
