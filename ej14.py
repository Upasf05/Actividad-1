print("Programa para obtener el signo zodiacal")
print("Introduce tu día y mes de nacimiento")
dia = int(input())
mes = input
if (mes == "marzo" and dia >= 21) or  (mes == "abril" and dia <= 19):
     signo = "Aries"
elif (mes == "marzo" and dia >= 20) or  (mes == "mayo" and dia <= 20):
     signo = "Aries"
elif (mes == "marzo" and dia >= 21) or  (mes == "junio" and dia <= 20):
     signo = "Tauro"
elif (mes == "marzo" and dia >= 21) or  (mes == "julio" and dia <= 22):
     signo = "Géminis"
elif (mes == "marzo" and dia >= 23) or  (mes == "agosto" and dia <= 22):
     signo = "Cáncer"
elif (mes == "marzo" and dia >= 23) or  (mes == "septiembre" and dia <= 22):
     signo = "Leo"
elif (mes == "marzo" and dia >= 23) or  (mes == "octubre" and dia <= 22):
     signo = "Virgo"
elif (mes == "marzo" and dia >= 23) or  (mes == "noviembre" and dia <= 21):
     signo = "Libra"
elif (mes == "marzo" and dia >= 22) or  (mes == "diciembre" and dia <= 21):
     signo = "Escorpio"
elif (mes == "marzo" and dia >= 22) or  (mes == "enero" and dia <= 19):
     signo = "Sagitario"
elif (mes == "marzo" and dia >= 20) or  (mes == "febrero" and dia <= 18):
     signo = "Capricornio"
else:
     signo = "Piscis"
