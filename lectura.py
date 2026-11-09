class Lectura:
    def __init__(self, codigo_origen: str, zona_nombre: str, hora: str, es_avistamiento: bool = False):
        self.codigo_origen = codigo_origen
        self.zona_nombre = zona_nombre
        self.hora = hora
        self.es_avistamiento = es_avistamiento