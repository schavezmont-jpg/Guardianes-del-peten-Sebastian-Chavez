from sistema_monitoreo import SistemaMonitoreo
from alerta import Alerta

def main():
    sistema = SistemaMonitoreo()

    print("==================================================")
    print("   GUARDIANES DEL PETÉN - COLAS Y PILAS (E6)")
    print("==================================================\n")

    # 1. Generar al menos cuatro alertas y agregarlas a la cola (y al sistema)
    a1 = Alerta("ALT-01", "Batería baja en collar de Balam", "alta", "10:00")
    a2 = Alerta("ALT-02", "Acercamiento a comunidad detectado", "media", "10:15")
    a3 = Alerta("ALT-03", "Movimiento atípico en sector norte", "alta", "10:30")
    a4 = Alerta("ALT-04", "Pérdida de señal temporal", "media", "10:45")

    for a in [a1, a2, a3, a4]:
        sistema.alertas.append(a)
        sistema.cola_alertas.encolar(a)

    print(f"--- 1. COLA DE ALERTAS (Total: {sistema.cola_alertas.tamanio()}) ---")
    siguiente_a = sistema.cola_alertas.siguiente()
    print(f"Siguiente alerta a atender: {siguiente_a}\n")

    # 2. Atender dos con atender_siguiente_alerta
    print("--- 2. ATENDIENDO DOS ALERTAS ---")
    sistema.atender_siguiente_alerta("GR-05")
    sistema.atender_siguiente_alerta("GR-05")
    print(f"Alertas restantes en cola: {sistema.cola_alertas.tamanio()}\n")

    # 3. Anotar al menos cuatro entradas en la bitácora, deshacer una y mostrar la bitácora completa
    print("--- 3. PRUEBAS DE BITÁCORA (PILA) ---")
    sistema.bitacora.registrar("Revisé la aguada Los Patos")
    sistema.bitacora.registrar("Calibré el collar del jaguar")
    sistema.bitacora.registrar("Reporte de ingreso de turistas erróneo")
    sistema.bitacora.registrar("Anuncio temporal de prueba equivocada")

    print("Bitácora antes de deshacer:")
    sistema.bitacora.mostrar()

    deshecha = sistema.bitacora.deshacer()
    print(f"\nAnotación deshecha (última): '{deshecha}'")

    print("\nBitácora completa actual (de más reciente a más antigua):")
    sistema.bitacora.mostrar()
    print("-" * 50)

    # 4. Atender hasta vaciar la cola y llamar una vez más a atender_siguiente_alerta
    print("\n--- 4. VACIANDO LA COLA DE ALERTAS ---")
    while not sistema.cola_alertas.esta_vacia():
        sistema.atender_siguiente_alerta("GR-01")

    print("Llamando a atender_siguiente_alerta con la cola ya vacía:")
    sistema.atender_siguiente_alerta("GR-01")
    print("==================================================")

if __name__ == "__main__":
    main()