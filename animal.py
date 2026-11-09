from abc import ABC, abstractmethod
import re

class Animal(ABC):
    def __init__(self, codigo: str, nombre: str, en_peligro: bool):
        self.codigo = codigo
        self.nombre = nombre
        self.en_peligro = en_peligro
        self.collar_asignado = None

    @abstractmethod
    def describir(self) -> str:
        """Método abstracto que obliga a cada hija a implementarlo."""
        pass

    def obtener_informacion_base(self) -> str:
        estado = "En peligro" if self.en_peligro else "No en peligro"
        return f"[{self.codigo}] {self.nombre} ({type(self).__name__}) - {estado}"

    @staticmethod
    def validar_formato_codigo(codigo: str) -> bool:
        patron = r'^[A-Z]{3}-\d{3}$'
        return bool(re.match(patron, codigo))