import re
from animal import Animal
from collar import Collar
from zona import Zona
from alerta import Alerta
from lectura import Lectura
from servicio_sms import ServicioSMS

class SistemaMonitoreo:
    def __init__(self):
        self.animales = []
        self.collares = []
        self.zonas = []
        self.alertas = []
        self.lecturas = []

    def buscar_animal(self, codigo: str):
        for a in self.animales:
            if a.codigo == codigo:
                return a
        return None

    def buscar_collar(self, codigo: str):
        for c in self.collares:
            if c.codigo == codigo:
                return c
        return None

    def buscar_zona(self, nombre: str):
        for z in self.zonas:
            if z.nombre.lower() == nombre.lower():
                return z
        return None

    @staticmethod
    def validar_codigo_gr(codigo_gr: str) -> bool:
        patron = r'^[A-Z]{2}-\d{2}$'
        return bool(re.match(patron, codigo_gr))

    def registrar_animal(self, codigo: str, nombre: str, especie: str) -> bool:
        if not Animal.validar_formato_codigo(codigo):
            print("  [RECHAZADO] Avisar: código inválido")
            return False
        if self.buscar_animal(codigo) is not None:
            print("  [RECHAZADO] Avisar: código repetido")
            return False
        print(f"  [ÉXITO] Animal {nombre} ({codigo}) procesado.")
        return True

    def ordenar_alertas(self):
        """Ordena las alertas por prioridad (alta primero, luego media) y por hora más temprana."""
        def nivel(alerta):
            if alerta.prioridad == "alta":
                return 1
            return 2

        n = len(self.alertas)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                nivel_min = nivel(self.alertas[min_idx])
                nivel_j = nivel(self.alertas[j])

                if nivel_j < nivel_min:
                    min_idx = j
                elif nivel_j == nivel_min:
                    if self.alertas[j].hora < self.alertas[min_idx].hora:
                        min_idx = j

            if min_idx != i:
                self.alertas[i], self.alertas[min_idx] = self.alertas[min_idx], self.alertas[i]

    def buscar_animal_binaria(self, codigo: str):
        """Busca un animal por su código usando Búsqueda Binaria sobre una lista ordenada por código."""
        self.animales.sort(key=lambda a: a.codigo)

        inicio = 0
        fin = len(self.animales) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            codigo_medio = self.animales[medio].codigo

            if codigo_medio == codigo:
                return self.animales[medio]
            elif codigo_medio < codigo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None