from animal import Animal

class MonoArana(Animal):
    def __init__(self, codigo: str, nombre: str, longitud_cola_cm: float):
        super().__init__(codigo, nombre, en_peligro=True)
        self.longitud_cola_cm = longitud_cola_cm

    def describir(self) -> str:
        return f"Mono Araña {self.nombre} ({self.codigo}): Primate arborícola, habita en la copa de los árboles, se balancea con su cola prensil (cola: {self.longitud_cola_cm} cm)."

    def balancearse(self) -> str:
        return f"El mono araña {self.nombre} se balancea hábilmente en las ramas."