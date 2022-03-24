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
        
ejercicio = CuentaBancaria("123", "Gonzalo", "24/03", "123456789", float(221.5))
ejercicio.retirar()
ejercicio.ingresar()
ejercicio.transferir()