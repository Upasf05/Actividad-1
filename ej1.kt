fun main () {
    println("Ingrese un número")
    val numero: Int = readLine()?.toIntOrNull()?:0
    if(numero>10){
        printIn("$numero es mayor a 10")
    }else {
        printIn("$numero es menor a 10")
    }
}
