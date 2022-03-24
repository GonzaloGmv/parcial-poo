class CuentaBancaria:
    def __init__(self, id, titular, apertura, numero_cuenta, saldo):
        self.id = id
        self.titular = titular
        self.apertura = apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    def retirar(self, dinero):
        if dinero > self.saldo:
            print("La cantidad de dinero a retirar es mayor que la del saldo")
        else:
            self.saldo = self.saldo - dinero
            print("Aquí está el dinero: ", dinero, "euros")
            print("Este es su saldo disponible: ", self.saldo, "euros")
    
    def ingresar(self, dinero):
        self.saldo = self.saldo + dinero
        print("Ha ingresado", dinero, "euros")
        print("Este es su saldo actual: ", self.saldo, "euros")
    
    def transferir(self, dinero):
        cuenta = input("Escriba el numero del cuenta al que quiere hacerle la transferencia: ")
        if dinero > self.saldo:
            print("La cantidad de dinero a transferir es mayor que la del saldo")
        else:
            self.saldo = self.saldo - dinero
            print("Se ha realizado la tranferencia de", dinero, "euros, a la cuenta", cuenta)
            print("Su saldo actual es", self.saldo)