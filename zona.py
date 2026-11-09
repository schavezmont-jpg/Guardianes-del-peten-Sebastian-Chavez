class Zona:
    TIPOS_VALIDOS = ["nucleo", "amortiguamiento", "uso multiple"]

    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo.lower()

    def es_tipo_valido(self) -> bool:
        return self.tipo in self.TIPOS_VALIDOS