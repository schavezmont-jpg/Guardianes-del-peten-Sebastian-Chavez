class BitacoraPatrulla:
    def __init__(self):
        self._anotaciones = []

    def registrar(self, entrada: str):
        """Pone la anotación encima (al final de la lista)."""
        self._anotaciones.append(entrada)

    def deshacer(self):
        """Saca y devuelve la última anotación. Si está vacía, devuelve None."""
        if self.esta_vacia():
            return None
        return self._anotaciones.pop()

    def ultima(self):
        """Devuelve la de encima sin sacarla. Si está vacía, devuelve None."""
        if self.esta_vacia():
            return None
        return self._anotaciones[-1]

    def esta_vacia(self) -> bool:
        """Devuelve True si la bitácora está vacía."""
        return len(self._anotaciones) == 0

    def mostrar(self):
        """Imprime las anotaciones de la más reciente a la más antigua."""
        if self.esta_vacia():
            print("  [Bitácora vacía]")
            return
        
        # Recorremos de atrás hacia adelante (LIFO)
        for i in range(len(self._anotaciones) - 1, -1, -1):
            print(f"  - {self._anotaciones[i]}")