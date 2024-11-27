fun main () {
    println("Ingrese un número")
    val numero: Int = readLine()?.toIntOrNull()?:0
    if(numero>1){
        printIn("Es positivo")
    } else if (numero == 0) {
        printIn("Es cero")
    } else {
        printIn("Es menor a 10")
    }
}
