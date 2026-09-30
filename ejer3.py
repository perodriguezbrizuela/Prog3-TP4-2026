usuarios = []

cantidad = int(input("¿Cuántos usuarios desea ingresar?: "))


for i in range(cantidad):

    print()
    print("Usuario", i + 1)

    usuario_info = {}


    usuario_info["nombre"] = input("Ingrese el nombre: ")

    usuario_info["edad"] = int(input("Ingrese la edad: "))

    usuario_info["direccion"] = input("Ingrese la dirección: ")

    usuario_info["telefono"] = input("Ingrese el teléfono: ")

    usuarios.append(usuario_info)


print("INFORMACIÓN DE LOS USUARIOS")

for usuario_info in usuarios:

    print("-----------------------------------")

    for clave, valor in usuario_info.items():

        print(clave, ":", valor)
