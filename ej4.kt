fun main () {
    println("Ingrese su nota")
    val numero: Double = readLine()?.toDoubleOrNull()?:0
    if(numero>7){
        printIn("Aprobó")
    } else {
        printIn("Reprobó")
    }
}
