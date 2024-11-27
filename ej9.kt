fun main () {
    println("Ingresar monto")
    val monto: double = readLine()?.toDoubleOrNull()?:0
    val descuento = if (compra > 100) compra 0.20 else 0.00
    val montoFinal = monto - descuento
        println("El monto inicial fue $monto")
        println("Si va a pagar más de $100, recibe un descuento, su monto final es $monto")
}
