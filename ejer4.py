sucursales = [
    {
        "nombre": "Sucursal 1",
        "instrumentos": [
            {"id": "001", "precio": 250000, "tipo": "Cuerda"},
            {"id": "002", "precio": 120000, "tipo": "Percusión"},
            {"id": "003", "precio": 180000, "tipo": "Viento"}
        ]
    },
    {
        "nombre": "Sucursal 2",
        "instrumentos": [
            {"id": "004", "precio": 300000, "tipo": "Cuerda"},
            {"id": "005", "precio": 150000, "tipo": "Percusión"},
            {"id": "006", "precio": 200000, "tipo": "Viento"},
            {"id": "007", "precio": 280000, "tipo": "Cuerda"}
        ]
    }
]


def listarInstrumentos():

    for sucursal in sucursales:

        for instrumento in sucursal["instrumentos"]:

            print(
                "Sucursal:", sucursal["nombre"],
                "| ID:", instrumento["id"],
                "| Precio:", instrumento["precio"],
                "| Tipo:", instrumento["tipo"]
            )


def instrumentosPorTipo(tipo):

    resultado = []

    for sucursal in sucursales:

        for instrumento in sucursal["instrumentos"]:


            if instrumento["tipo"].lower() == tipo.lower():

                resultado.append(instrumento)


    return resultado



def borrarInstrumento(id):

    for sucursal in sucursales:

        for instrumento in sucursal["instrumentos"]:

            if instrumento["id"] == id:

                sucursal["instrumentos"].remove(instrumento)

                print("Instrumento eliminado correctamente.")

                return


    print("No se encontró un instrumento con ese ID.")


def porcInstrumentosPorTipo(sucursal):

    for suc in sucursales:

        if suc["nombre"].lower() == sucursal.lower():

            instrumentos = suc["instrumentos"]


            total = len(instrumentos)

            if total == 0:
                print("La sucursal no tiene instrumentos.")
                return

            percusion = 0
            viento = 0
            cuerda = 0


            for instrumento in instrumentos:

                if instrumento["tipo"] == "Percusión":
                    percusion += 1

                elif instrumento["tipo"] == "Viento":
                    viento += 1

                elif instrumento["tipo"] == "Cuerda":
                    cuerda += 1


            porcentaje_percusion = (percusion / total) * 100
            porcentaje_viento = (viento / total) * 100
            porcentaje_cuerda = (cuerda / total) * 100

            print("Sucursal:", sucursal)
            print("Percusión:", porcentaje_percusion, "%")
            print("Viento:", porcentaje_viento, "%")
            print("Cuerda:", porcentaje_cuerda, "%")

            return

    print("No se encontró la sucursal.")

print("-----------------------")
print("LISTA DE INSTRUMENTOS")
print("-----------------------")
listarInstrumentos()

print("-----------------------")
print("INSTRUMENTOS DE CUERDA")
print("-----------------------")

instrumentos_cuerda = instrumentosPorTipo("Cuerda")

for instrumento in instrumentos_cuerda:
    print(instrumento)

print("-----------------------")
print("BORRAR INSTRUMENTO")
print("-----------------------")

borrarInstrumento("001")

print("-----------------------")
print("LISTA DESPUÉS DE BORRAR")
print("-----------------------")

listarInstrumentos()

print("-----------------------")
print("PORCENTAJES POR TIPO")
print("-----------------------")

porcInstrumentosPorTipo("Sucursal 1")
print("-----------------------")
print("-----------------------")
porcInstrumentosPorTipo("Sucursal 2")