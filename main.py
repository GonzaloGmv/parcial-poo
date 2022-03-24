from ejr4.cuenta_bancaria import CuentaBancaria
from ejr4.plazo_fijo import CuentaPlazoFijo
from ejr4.cuenta_vip import CuentaVip
import random

if __name__ == "__main__":
    cuenta = input("Escriba el tipo de cuenta que tiene (cuenta bancaria, plazo fijo, vip): ")
    if cuenta == "cuenta bancaria":
        ejercicio = CuentaBancaria(int(1234), "Gonzalo", "7/23", "123456789102", float(10000))
        ejercicio.transferir(float(2000))
        ejercicio.ingresar(float(575))
        ejercicio.retirar(float(78))

    elif cuenta == "plazo fijo":
        ejercicio = CuentaPlazoFijo(int(1234), "Gonzalo", "7/23", "123456789102", float(10000), "7/24")
        ejercicio.transferir(float(2000))
        ejercicio.ingresar(float(575))
        ejercicio.retirar(float(78))
    
    elif cuenta == "vip":
        ejercicio = CuentaVip(int(1234), "Gonzalo", "7/23", "123456789102", float(10000), float(10000))
        ejercicio.transferir(float(2000))
        ejercicio.ingresar(float(575))
        ejercicio.retirar(float(78))
    
    else:
        print("Ese tipo de cuenta no existe")