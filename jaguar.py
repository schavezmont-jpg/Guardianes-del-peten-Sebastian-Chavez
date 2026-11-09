from animal import Animal

class Jaguar(Animal):
    def __init__(self, codigo: str, nombre: str, territorio_km2: float):
        super().__init__(codigo, nombre, en_peligro=True)
        self.territorio_km2 = territorio_km2

    def describir(self) -> str:
        return f"Jaguar {self.nombre} ({self.codigo}): Felino carnívoro, habita en zona núcleo y de amortiguamiento, cubre un territorio de {self.territorio_km2} km²."

    def rugir(self) -> str:
        return f"El jaguar {self.nombre} emite un potente rugido."