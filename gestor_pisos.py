import json
from typing import List

# 👤 Clase Residente
class Residente:
    def __init__(self, nombre: str, profesion: str):
        self.nombre = nombre
        self.profesion = profesion

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "profesion": self.profesion
        }

# 🏡 Clase Vivienda
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

# 💾 Guardar viviendas en archivo
def guardar_viviendas(viviendas: List[Vivienda], archivo="viviendas.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([v.to_dict() for v in viviendas], f, indent=4, ensure_ascii=False)

# 🔁 Cargar viviendas usando json.loads
def cargar_viviendas(archivo="viviendas.json") -> List[Vivienda]:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()                  # Leer texto completo
            data = json.loads(texto)          # Cargar como objeto Python
            viviendas = []
            for v in data:
                vivienda = Vivienda(v["localidad"], v["calle"], v["numero"], v["codigo"])
                for r in v.get("residentes", []):
                    vivienda.agregar_residente(Residente(r["nombre"], r["profesion"]))
                viviendas.append(vivienda)
            return viviendas
    except FileNotFoundError:
        return []

# 🚀 Prueba rápida
if __name__ == "__main__":
    # Crear viviendas y residentes
    v1 = Vivienda("Bilbao", "Av. del Norte", 10, "A10")
    v2 = Vivienda("Toledo", "Calle Vieja", 45, "B22")

    v1.agregar_residente(Residente("Nuria", "Diseñadora"))
    v2.agregar_residente(Residente("Carlos", "Electricista"))
    v2.agregar_residente(Residente("Eva", "Administrativa"))

    # Trasladar a Eva desde v2 → v1
    v2.mover_residente("Eva", v1)

    # Guardar en archivo
    guardar_viviendas([v1, v2])

    # Leer desde archivo y mostrar
    viviendas = cargar_viviendas()
    for v in viviendas:
        print(f"\n🏠 {v.codigo} - {v.localidad}, {v.calle} {v.numero}")
        for r in v.residentes:
            print(f"   👤 {r.nombre} - {r.profesion}")