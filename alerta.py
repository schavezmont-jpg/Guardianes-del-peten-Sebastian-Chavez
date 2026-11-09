class Alerta:
    def __init__(self, tipo: str, prioridad: str, detalle: str, hora: str = "00:00"):
        self.tipo = tipo
        self.prioridad = prioridad.lower()
        self.detalle = detalle
        self.hora = hora
        self.atendida = False
        self.atendida_por = None

    def atender(self, codigo_gr: str) -> bool:
        if self.atendida:
            return False
        self.atendida = True
        self.atendida_por = codigo_gr
        return True