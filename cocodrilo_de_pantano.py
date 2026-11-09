from animal import Animal

class CocodriloDePantano(Animal):
    def __init__(self, codigo: str, nombre: str, largo_metros: float):
        super().__init__(codigo, nombre, en_peligro=False)  # Art. 2: No en peligro
        self.largo_metros = largo_metros

    def describir(self) -> str:
        return f"Cocodrilo de Pantano {self.nombre} ({self.codigo}): Reptil carnívoro, habita en lagunas y humedales, se desplaza reptando y nadando (largo: {self.largo_metros} m)."

    def asolearse(self) -> str:
        return f"El cocodrilo {self.nombre} se asolea en la ribera."