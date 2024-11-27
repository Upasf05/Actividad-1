def nprimo(num):
       if num <= 1:
             return False
       for i in range(2, int(num  ** 0.5) + 1):
             if num % i == 0:
                   return False
       return True
primos = ""
for i in range(1, 51):
      if nprimo(i):
            primos += str(i) + " "
print("Números primos entre 1 y 50: " + primos.strip())

