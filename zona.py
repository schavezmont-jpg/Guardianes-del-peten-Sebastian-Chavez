class Zona:
    def __init__(self, nombre: str, descripcion: str = ""):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subzonas = []   # Lista que almacena subzonas (recursividad)
        self.animales = []   # Lista de animales ubicados en esta zona exacta

    def agregar_subzona(self, subzona):
        """Agrega una subzona a la lista de subzonas."""
        self.subzonas.append(subzona)

    def ubicar(self, animal):
        """Ubica un animal en esta zona."""
        self.animales.append(animal)

    def mostrar(self, nivel: int = 0):
        """Muestra la zona de forma recursiva con una sangría de dos espacios por cada nivel."""
        sangria = "  " * nivel
        print(f"{sangria}- Zona: {self.nombre} ({self.descripcion}) [Animales: {len(self.animales)}]")
        for sub in self.subzonas:
            sub.mostrar(nivel + 1)

    def contar_animales(self) -> int:
        """Devuelve los animales de esta zona más los de todas sus subzonas recursivamente."""
        total = len(self.animales)
        for sub in self.subzonas:
            total += sub.contar_animales()
        return total

    def buscar_sector(self, nombre: str):
        """Busca un sector de forma recursiva por nombre (caso base y llamadas a subzonas)."""
        if self.nombre.lower() == nombre.lower():
            return self
        
        for sub in self.subzonas:
            resultado = sub.buscar_sector(nombre)
            if resultado is not None:
                return resultado
                
        return None