from Cliente import Cliente
from Cuenta import Cuenta

print("Banco el Wilmar y el York")

nombre=input("Nombre: ")
apellido=input("Apellido: ")
cedula=input("Cedula: ")
ciudad=input("Ciudad: ")
NumeroCuenta=input("Numero de cuenta: ")
saldo=float(input("Saldo: "))
cliente=Cliente(nombre, apellido, cedula, ciudad)
cuenta=Cuenta(NumeroCuenta,saldo)

print("1. consultar saldo")
print("2. retirar dinero")
print("3. depositar dinero")
print("4. Salir")
      
def menu():
    return int(input("Digite la opcion: "))
def retirar(retirar):
    total=cuenta.get_saldo()-retirar
    cuenta.set_saldo(total)

def depositar(depositar):
    total=cuenta.get_saldo()+depositar
    cuenta.set_saldo(total)

salir=False
while not salir:
    opcion=menu()
    if opcion==1:
        print(f" Señor {cliente.nombre} su saldo es de  ${cuenta.get_saldo()}")
    elif opcion==2:
        valorRetiro=float(input("Cantidad de dinero a retirar: "))
        if (valorRetiro > cuenta.get_saldo() ):
            print("Saldo insuficiente en su cuenta")
        else:
           retirar(valorRetiro)
           print(f"Retiro exitoso por ${valorRetiro}")
           print(f"Ahora su saldo es de ${cuenta.get_saldo()} ") 

    elif opcion==3:
        deposito=float(input("Cantidad de dinero a depositar: "))
        depositar(deposito)
        print(f"Deposito exitoso por ${deposito}")
        print(f"Ahora su saldo es de ${cuenta.get_saldo()} ")
    
    elif opcion==4:
        salir=True
        print(f"Hasta luego {cliente.nombre}!!")
    else:
        print("Digita una opcion valida")