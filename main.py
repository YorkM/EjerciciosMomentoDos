
from Clases.Cliclista import Ciclista

ciclista = Ciclista()
ciclista.ciclistas = ([])
tiemposCiclistas=[]
merjorTiempo=None
menu = 1


while(menu != 0):
    print("Presione 1 para ingresar un ciclista")
    print("Precione 0 para salir")
    menu = int(input("Digite una opcion: "))

    if(menu == 1):
        opcion = 1

        while(opcion == 1):
            ciclista.nombre = input("Digite el nombre: ")
            ciclista.edad = int(input("Digite la edad: "))
            ciclista.pais = input("Digite el pais: ")
            ciclista.equipo = input("Digite el equipo: ")
            ciclista.tiempo = int(input("Digite el tiempo en minutos: "))
            print("")
            print("****************************************************")

            ciclista.ciclistas.append([ciclista.nombre,ciclista.edad,ciclista.pais,ciclista.equipo,ciclista.tiempo])
            print("Presione 1 para ingresar un nuevo ciclista")
            print("Precione 0 para salir")
            opcion = int(input("Digite una opcion: "))
            menu = opcion
    elif(menu!=0):
        print("Debes ingresar una opcion valida")
else:
    print("")
    print("Muchas gracias")
    print("")


for i in range(0, len(ciclista.ciclistas)):
    tiemposCiclistas.append(ciclista.ciclistas[i][4])

menorTiempo = min(tiemposCiclistas)
imejorTiempo = tiemposCiclistas.index(menorTiempo)
     
print("*********************************************")
print("El ciclista con el mejor tiempo es:")
print("Nombre: ",ciclista.ciclistas[imejorTiempo][0])
print("Edad: ", ciclista.ciclistas[imejorTiempo][1])
print("Pais: ",ciclista.ciclistas[imejorTiempo][2])
print("Equipo: ",ciclista.ciclistas[imejorTiempo][3])
print("Con un tiempo de: ",ciclista.ciclistas[imejorTiempo][4])
print("*****FELICITACIONES*****")
