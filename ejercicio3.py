class CuentaBancaria:
    def __init__(self, titular:str, saldo:float):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto:float):
        if monto <= 0:
            print("Ingrese un monto válido")
            return
        self.saldo = self.saldo + monto
        print(f"Se agregaron L{monto} a su cuenta, su nuevo saldo es: L{self.saldo}")
    
    def retirar(self, monto:float):
        if monto > self.saldo:
            print("No es posible realizar la transacción ya que su saldo es demasiado bajo")
            return
        self.saldo = self.saldo - monto
        print(f"Se retiraron L{monto} de su cuenta, su nuevo saldo es: L{self.saldo}")

    def mostrar_saldo(self):
        print(f"Hola: {self.titular}\nEl saldo actual de su cuenta es: L{self.saldo}")

cuenta1 = CuentaBancaria("Raquel Alvarado", 2560)
cuenta1.mostrar_saldo()
cuenta1.retirar(300)
cuenta1.depositar(10000)
cuenta1.mostrar_saldo()
cuenta1.retirar(20000)
cuenta1.depositar(-200)
