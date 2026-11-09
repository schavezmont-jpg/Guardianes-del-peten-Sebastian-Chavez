from animal import Animal

class Tapir(Animal):
    def __init__(self, codigo: str, nombre: str, peso_promedio_kg: float):
        super().__init__(codigo, nombre, en_peligro=True)
        self.peso_promedio_kg = peso_promedio_kg

    def describir(self) -> str:
        return f"Tapir {self.nombre} ({self.codigo}): Mamífero herbívoro, habita en la selva tropical cerca de ríos, se desplaza caminando y nadando (peso: {self.peso_promedio_kg} kg)."

    def nadar(self) -> str:
        return f"El tapir {self.nombre} se adentra a nadar en el río."