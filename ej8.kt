if  (numero3 > mayor) {
    mayor = num3
    }
    fun main () {
           println("Ingrese su edad")
           val edad: int = readLine()?.toIntOrNull()?:0
           if(edad>18){
               println("Es adulto")
           } else if (edad >13) {
               println("Es adolescente")
           } else {
               println("Es niño")
           }
    }
    