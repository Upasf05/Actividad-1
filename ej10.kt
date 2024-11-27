fun main () {
    println("Ingresar números")
    val num1: Double = readLine ()?.toDoubleOrNull() ?: 0
    val num2: Double = readLine ()?.toDoubleOrNull() ?: 0
    println("Ingresar operación, puede ser suma, resta, mult o div")
    val operación = readLine()
    val resultado = when operacion {
           "suma" -> num1 + num2
           "resta" -> num1 - num2
           "mult" -> num1 * num2
           "div" -> num1 / num2
      }
     println("El resultado de la operación fue $resultado")
}
