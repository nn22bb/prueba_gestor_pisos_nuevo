import json
from typing import List

# 🧍 Clase Persona
class Residente:
    def __init__(self, nombre: str, profesion: str):
        self.nombre = nombre
        self.profesion = profesion

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "profesion": self.profesion
        }

# 🏠 Clase Vivienda
class Vivienda:
    def __init__(self, localidad: str, calle: str, numero: int, codigo: str):
        self.localidad = localidad
        self.calle = calle
        self.numero = numero
        self.codigo = codigo
        self.residentes: List[Residente] = []

    def agregar_residente(self, residente: Residente):
        self.residentes.append(residente)

    def quitar_residente(self, nombre: str):
        self.residentes = [r for r in self.residentes if r.nombre != nombre]

    def mover_residente(self, nombre: str, otra_vivienda):
        for r in self.residentes:
            if r.nombre == nombre:
                otra_vivienda.agregar_residente(r)
                self.quitar_residente(nombre)
                break

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "localidad": self.localidad,
            "calle": self.calle,
            "numero": self.numero,
            "residentes": [r.to_dict() for r in self.residentes]
        }

# 🔁 Guardar y cargar desde archivo
def guardar_viviendas(viviendas: List[Vivienda], archivo="viviendas.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([v.to_dict() for v in viviendas], f, indent=4, ensure_ascii=False)

def cargar_viviendas(archivo="viviendas.json") -> List[Vivienda]:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            viviendas = []
            for v in data:
                vivienda = Vivienda(v["localidad"], v["calle"], v["numero"], v["codigo"])
                for r in v.get("residentes", []):
                    vivienda.agregar_residente(Residente(r["nombre"], r["profesion"]))
                viviendas.append(vivienda)
            return viviendas
    except FileNotFoundError:
        return []

# 🚀 Demo rápida
if __name__ == "__main__":
    # Crear viviendas
    v1 = Vivienda("Valencia", "Sol Naciente", 101, "A1")
    v2 = Vivienda("Sevilla", "Calle Luna", 204, "B3")

    # Añadir residentes
    v1.agregar_residente(Residente("Sofía", "Arquitecta"))
    v1.agregar_residente(Residente("Mario", "Panadero"))

    v2.agregar_residente(Residente("Lucía", "Enfermera"))

    # Simular traslado
    v1.mover_residente("Mario", v2)

    # Guardar
    guardar_viviendas([v1, v2])

    # Ver resultado
    viviendas = cargar_viviendas()
    for v in viviendas:
        print(f"🏡 Vivienda en {v.localidad}, {v.calle} {v.numero}")
        for r in v.residentes:
            print(f"   👤 {r.nombre} - {r.profesion}")