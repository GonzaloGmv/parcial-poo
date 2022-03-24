from ejr4.cuenta_bancaria import CuentaBancaria

class CuentaPlazoFijo(CuentaBancaria):
    def __init__(self, id, titular, apertura, numero_cuenta, saldo, fecha_vencimiento):
        super().__init__(id, titular, apertura, numero_cuenta, saldo)
        self.fecha_vencimiento = fecha_vencimiento

    def retirar(self, dinero):
        if self.fecha_vencimiento > self.apertura:
            if dinero > self.saldo:
                print("La cantidad de dinero a retirar es mayor que la del saldo")
            else:
                self.saldo = self.saldo - dinero
                self.saldo = self.saldo * 0.95
                print("Aquí está el dinero: ", dinero, "euros")
                print("Este es su saldo disponible: ", self.saldo, "euros")
        else:
            super().retirar(dinero)

    def ingresar(self, dinero):
        super().ingresar(dinero)
    
    def transferir(self, dinero):
        super().transferir(dinero)