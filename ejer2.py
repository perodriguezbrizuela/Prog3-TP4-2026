
usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}

administradores = {"Juan", "Marcela"}

administradores.discard("Juan")

administradores.add("Marcos")


print("Lista de usuarios:")


for usuario in usuarios:

    if usuario in administradores:
        print(usuario, "es Administrador")
    else:
        print(usuario, "es Usuario común")