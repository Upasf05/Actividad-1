def sumadigitos(n):
       suma = 0
       while n> 0:
               suma += n % 10
               n //= 10
       return suma
print("Ingresa un número")
numero = int(input())
resultado = sumadigitos(numero)
print("Los dígitos de " + str(numero) + " sumados dan " + str(resultado))
