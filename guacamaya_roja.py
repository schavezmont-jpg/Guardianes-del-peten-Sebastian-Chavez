from animal import Animal

class GuacamayaRoja(Animal):
    def __init__(self, codigo: str, nombre: str, envergadura_alas_cm: float):
        super().__init__(codigo, nombre, en_peligro=True)
        self.envergadura_alas_cm = envergadura_alas_cm

    def describir(self) -> str:
        return f"Guacamaya Roja {self.nombre} ({self.codigo}): Ave frugívora, habita en el dosel alto de los árboles, vuela en bandadas (envergadura: {self.envergadura_alas_cm} cm)."

    def volar_en_bandada(self) -> str:
        return f"La guacamaya {self.nombre} vuela por el dosel."