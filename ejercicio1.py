numeros=[1,3,4,7,9]
bandera=1
numero=0

while bandera==1:
    numero=int(input("Ingrese un numero del 0 al 9 para ver si está en la lista:"))
    if numero<0 or numero>9:
        print("Ingreso un numero fuera del rango")
    else:
        if numero in numeros:
            print("el numero está en la lista")
        else:
            print("el numeor no esta en la lista")
    
    bandera=int(input("quiere ingresar otro numero? 1-SI 2-NO:"))
    if bandera != 1:
        print("se cierra el programa")
        bandera=5


