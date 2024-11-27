fun main () {
    println("Bienvenido al sistema de votaciones")
    println("Este programa verá si tiene la edad mínima para votar")
    val numero: int = readLine()?.toIntOrNull()?:0
    if(numero>18){
        println("Puedes votar")
    } else {
        println("Aún no puedes votar")
    }
}

