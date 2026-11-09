class ServicioSMS:
    @staticmethod
    def enviar_mensaje(destino: str, mensaje: str):
        print(f"  [SMS ENVIADO a {destino}]: {mensaje}")