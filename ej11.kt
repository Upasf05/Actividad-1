fun main () {
    println("Calculadora de años bisiestos. Un año bisiesto, que se da cada 4 años, tiene un día más al finalizar el mes de febrero")
    val year: Int= readLine ()?.toIntOrNull() ?: 0
    val bisiesto = when {
          year % 400 == 0 -> true
          year % 100 == 0 -> false
          year % 4 === 0 -> true
          else -> false
     }
     println("El año $year ${if (bisiesto) "es" else "no es"} bisiesto")
}
