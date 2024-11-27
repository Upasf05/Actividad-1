fun main () {
    println("Ingresar monto")
    val monto: Double = readLine()?.toDoubleOrNull()?:0
    val descuento = if (compra > 100) compra 0.20 else 0.00
    val montoFinal = monto – descuento
        printIn("El monto inicial fue $monto")
        printIn("Si va a pagar más de $100, recibe un descuento, su monto final es $monto")
}

