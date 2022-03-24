class CuentaBancaria:
    def __init__(self, id, titular, apertura, numero_cuenta, saldo):
        self.id = id
        self.titular = titular
        self.apertura = apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    def retirar(self):
        dinero = float(input("Escriba la cantidad que desea retirar: "))
        if dinero > self.saldo:
            print("La cantidad de dinero a retirar es mayor que la del saldo")
        else:
            self.saldo = self.saldo - dinero
            print("Aquí está el dinero: ", dinero, "euros")
            print("Este es su saldo disponible: ", self.saldo, "euros")
    
    def ingresar(self):
        dinero = float(input("Escriba la cantidad de dinero que desea ingresar: "))
        self.saldo = self.saldo + dinero
        print("Este es su saldo actual: ", self.saldo, "euros")
    
    def transferir(self):
        cuenta = input("Escriba el numero del cuenta al que quiere hacerle la transferencia: ")
        dinero = float(input("Escriba la cantidad que desea transferir: "))
        if dinero > self.saldo:
            print("La cantidad de dinero a transferir es mayor que la del saldo")
        else:
            self.saldo = self.saldo - dinero
            print("Se ha realizado la tranferencia de", dinero, "euros, a la cuenta", cuenta)
            print("Su saldo actual es", self.saldo)
        
class CuentaPlazoFijo(CuentaBancaria):
    def __init__(self, id, titular, apertura, numero_cuenta, saldo, fecha_vencimiento):
        super().__init__(id, titular, apertura, numero_cuenta, saldo)
        self.fecha_vencimiento = fecha_vencimiento

    def retirar(self):
        if self.fecha_vencimiento > self.apertura:
            dinero = float(input("Escriba la cantidad que desea retirar: "))
            if dinero > self.saldo:
                print("La cantidad de dinero a retirar es mayor que la del saldo")
            else:
                self.saldo = self.saldo - dinero
                self.saldo = self.saldo * 0.95
                print("Aquí está el dinero: ", dinero, "euros")
                print("Este es su saldo disponible: ", self.saldo, "euros")
        else:
            super().retirar()

    def ingresar(self):
        super().ingresar()
    
    def transferir(self):
        super().transferir()

#ejercicio = CuentaPlazoFijo("123", "Gonzalo", "7/23", "1345", float(154.12), "7/22")
#ejercicio.ingresar()
