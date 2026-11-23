class ColaAlertas:
    def __init__(self):
        self._elementos = []

    def encolar(self, alerta):
        """Agrega la alerta al final de la cola."""
        self._elementos.append(alerta)

    def atender(self):
        """Saca y devuelve la alerta del frente (la más antigua). Si está vacía, devuelve None."""
        if self.esta_vacia():
            return None
        return self._elementos.pop(0)

    def siguiente(self):
        """Devuelve la alerta del frente sin sacarla. Si está vacía, devuelve None."""
        if self.esta_vacia():
            return None
        return self._elementos[0]

    def esta_vacia(self) -> bool:
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return len(self._elementos) == 0

    def tamanio(self) -> int:
        """Devuelve la cantidad de elementos en la cola."""
        return len(self._elementos)