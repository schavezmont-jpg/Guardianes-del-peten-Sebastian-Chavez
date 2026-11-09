class Collar:
    def __init__(self, codigo: str, bateria: int):
        self.codigo = codigo
        self.bateria = bateria
        self.animal_asignado = None

    def tiene_bateria_suficiente(self) -> bool:
        return self.bateria >= 10