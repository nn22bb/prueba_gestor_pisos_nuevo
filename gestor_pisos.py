import json
import os

ARCHIVO_DATOS = "pisos.json"

# Cargar datos desde archivo
def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return {}
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
        return json.load(f)

# Guardar datos a archivo
def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Ver todos los pisos
def ver_pisos(datos):
    if not datos:
        print("No hay pisos registrados aún.")
        return
    for id_piso, piso in datos.items():
        print(f"Piso {id_piso}: {piso['ciudad']}, {piso['calle']} {piso['numero']}")
        for inq in piso["inquilinos"]:
            print(f"   → {inq['nombre']} ({inq['trabajo']})")
        print()

# Ver inquilinos de un piso
def ver_inquilinos(datos, id_piso):
    piso = datos.get(id_piso)
    if piso:
        if piso["inquilinos"]:
            print(f"Inquilinos del piso {id_piso}:")
            for inq in piso["inquilinos"]:
                print(f" - {inq['nombre']} ({inq['trabajo']})")
        else:
            print("Este piso no tiene inquilinos.")
    else:
        print("Piso no encontrado.")

# Añadir nuevo inquilino
def añadir_inquilino(datos, id_piso, nombre, trabajo):
    if id_piso in datos:
        datos[id_piso]["inquilinos"].append({"nombre": nombre, "trabajo": trabajo})
    else:
        print("Ese piso no existe.")

# Mover inquilino a otro piso
def mover_inquilino(datos, origen, destino, nombre):
    if origen not in datos or destino not in datos:
        print("Piso origen o destino no encontrado.")
        return
    inquilino = None
    for i, p in enumerate(datos[origen]["inquilinos"]):
        if p["nombre"] == nombre:
            inquilino = datos[origen]["inquilinos"].pop(i)
            break
    if inquilino:
        datos[destino]["inquilinos"].append(inquilino)
    else:
        print("Inquilino no encontrado en el piso origen.")

# Eliminar inquilino
def eliminar_inquilino(datos, id_piso, nombre):
    piso = datos.get(id_piso)
    if piso:
        antes = len(piso["inquilinos"])
        piso["inquilinos"] = [i for i in piso["inquilinos"] if i["nombre"] != nombre]
        if len(piso["inquilinos"]) < antes:
            print("✔️ Inquilino eliminado.")
        else:
            print("Inquilino no encontrado.")
    else:
        print("Piso no encontrado.")

# Crear nuevo piso
def crear_piso(datos, id_piso, ciudad, calle, numero):
    if id_piso in datos:
        print("Ese ID de piso ya existe.")
    else:
        datos[id_piso] = {
            "ciudad": ciudad,
            "calle": calle,
            "numero": numero,
            "inquilinos": []
        }
        print("✔️ Piso creado correctamente.")

# Menú interactivo
def menu():
    datos = cargar_datos()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE PISOS ---")
        print("1. Ver todos los pisos")
        print("2. Ver inquilinos de un piso")
        print("3. Crear nuevo piso")
        print("4. Añadir inquilino a un piso")
        print("5. Mover inquilino a otro piso")
        print("6. Eliminar inquilino")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_pisos(datos)
        elif opcion == "2":
            id_piso = input("ID del piso: ")
            ver_inquilinos(datos, id_piso)
        elif opcion == "3":
            id_piso = input("Nuevo ID de piso: ")
            ciudad = input("Ciudad: ")
            calle = input("Calle: ")
            numero = input("Número: ")
            crear_piso(datos, id_piso, ciudad, calle, numero)
        elif opcion == "4":
            id_piso = input("ID del piso: ")
            nombre = input("Nombre del inquilino: ")
            trabajo = input("Trabajo: ")
            añadir_inquilino(datos, id_piso, nombre, trabajo)
        elif opcion == "5":
            origen = input("ID del piso actual: ")
            destino = input("ID del nuevo piso: ")
            nombre = input("Nombre del inquilino: ")
            mover_inquilino(datos, origen, destino, nombre)
        elif opcion == "6":
            id_piso = input("ID del piso: ")
            nombre = input("Nombre del inquilino: ")
            eliminar_inquilino(datos, id_piso, nombre)
        elif opcion == "0":
            guardar_datos(datos)
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❗ Opción no válida.")

# Ejecutar menú
if __name__ == "__main__":
    menu()