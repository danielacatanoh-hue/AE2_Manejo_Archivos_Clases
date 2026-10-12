
import json
from pathlib import Path



class ManejadorJSON:
    """Lee, modifica y guarda registros JSON en formato JSON Lines."""

    def __init__(self, ruta_archivo):
        self.ruta_archivo = Path(ruta_archivo)
        self.datos = []
        self.modificaciones = []

    @property
    def cantidad_registros(self):
        return len(self.datos)



    def importar(self):
        """Lee un objeto JSON por cada línea del archivo."""
        self.datos = []

        with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                if linea.strip():
                    try:
                        registro = json.loads(linea)
                    except json.JSONDecodeError as error:
                        raise ValueError(
                            f"Error JSON en la línea {numero_linea}: {error}"
                        ) from error

                    if not isinstance(registro, dict):
                        raise TypeError(
                            f"La línea {numero_linea} no contiene un objeto JSON."
                        )

                    self.datos.append(registro)

        return self.datos

    def actualizar_valor(self, indice, campo, valor_nuevo):
        """Modifica un campo de un registro."""
        if not self.datos:
            self.importar()

        if indice < 0 or indice >= len(self.datos):
            raise IndexError("El índice está fuera del rango.")

        if campo not in self.datos[indice]:
            raise KeyError(f"El campo '{campo}' no existe.")

        valor_anterior = self.datos[indice][campo]
        self.datos[indice][campo] = valor_nuevo

        self.modificaciones.append(
            f"Registro {indice}, campo '{campo}': "
            f"'{valor_anterior}' -> '{valor_nuevo}'"
        )

        return valor_anterior, valor_nuevo

    def guardar(self, ruta_salida):
        """Guarda los registros en formato JSON Lines."""
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        with ruta_salida.open("w", encoding="utf-8") as archivo:
            for registro in self.datos:
                archivo.write(
                    json.dumps(registro, ensure_ascii=False) + "\n"
                )

        return ruta_salida

    def obtener_resumen(self):
        """Devuelve un resumen de la importación y las modificaciones."""
        return {
            "archivo": str(self.ruta_archivo),
            "total_registros": len(self.datos),
            "total_modificaciones": len(self.modificaciones),
            "modificaciones": self.modificaciones.copy(),
        }
