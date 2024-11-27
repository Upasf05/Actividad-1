fun main() {
    println("Ingresa un número")
    val numero: Int = readLine()?.toIntOrNull()?:0
    if (numero% 2 == 0) {
         printIn ("Es par")
     } else {
         printIn ("No es par")
     }
}
