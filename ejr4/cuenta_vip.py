from ejr4.cuenta_bancaria import CuentaBancaria

class CuentaVip(CuentaBancaria):
    def __init__(self, id, titular, apertura, numero_cuenta, saldo, saldo_negativo):
        super().__init__(id, titular, apertura, numero_cuenta, saldo)
        self.saldo_negativo = saldo_negativo

    def retirar(self, dinero):
        if dinero > self.saldo + self.saldo_negativo:
            print("Superaría el saldo negativo maximo establecido")
        else:
            self.saldo = self.saldo - dinero
            print("Aquí está el dinero:", dinero, "euros")
            print("Este es su saldo disponible:", self.saldo, "euros")

    def ingresar(self, dinero):
        super().ingresar(dinero)
    
    def transferir(self, dinero):
        cuenta = input("Escriba el numero del cuenta al que quiere hacerle la transferencia: ")
        if dinero > self.saldo + self.saldo_negativo:
            print("Superaría el saldo negativo maximo establecido")
        else:
            self.saldo = self.saldo - dinero
            print("Se ha realizado la tranferencia de", dinero, "euros, a la cuenta", cuenta)
            print("Su saldo actual es", self.saldo)