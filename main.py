from sistema_monitoreo import SistemaMonitoreo
from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano
from mono_arana import MonoArana
from alerta import Alerta

def main():
    sistema = SistemaMonitoreo()

    print("==================================================")
    print("   GUARDIANES DEL PETÉN - ORDENAR Y BUSCAR (E4)")
    print("==================================================\n")

    # 1. Instanciar animales (asegurando códigos para probar orden y búsqueda)
    balam = Jaguar("JAG-001", "Balam", 150.5)
    tziquin = Tapir("TAP-001", "Tziquin", 250.0)
    scarlet = GuacamayaRoja("GUA-001", "Scarlet", 90.0)
    sobek = CocodriloDePantano("COC-001", "Sobek", 3.5)
    kaan = MonoArana("MON-001", "Kaan", 80.0)

    sistema.animales.extend([balam, tziquin, scarlet, sobek, kaan])

    # 2. PRUEBA DE ORDENAMIENTO DE ALERTAS (Selección)
    print("--- 1. PRUEBA DE ORDENAMIENTO DE ALERTAS ---")
    # Crear al menos cinco alertas en desorden (altas y medias, con horas distintas)
    sistema.alertas = [
        Alerta("Batería baja", "media", "Collar COL-003", "14:30"),
        Alerta("Acercamiento", "alta", "Jaguar en zona poblada", "08:15"),
        Alerta("Batería baja", "media", "Collar COL-001", "09:00"),
        Alerta("Caza ilegal", "alta", "Disparo detectado sector norte", "06:45"),
        Alerta("Intrusión", "media", "Zona núcleo violada", "11:20")
    ]

    print("Alertas ANTES de ordenar:")
    for a in sistema.alertas:
        print(f"  [{a.prioridad.upper()}] - Hora: {a.hora} - {a.detalle}")

    sistema.ordenar_alertas()

    print("\nAlertas DESPUÉS de ordenar (por selección: Altas primero, luego Medias, por hora):")
    for a in sistema.alertas:
        print(f"  [{a.prioridad.upper()}] - Hora: {a.hora} - {a.detalle}")
    print("-" * 50)

    # 3. PRUEBA DE BÚSQUEDA BINARIA DE ANIMALES
    print("\n--- 2. PRUEBA DE BÚSQUEDA BINARIA POR CÓDIGO ---")
    
    # Listar animales ordenados para referencia
    sistema.animales.sort(key=lambda x: x.codigo)
    print("Lista de códigos de animales ordenados:")
    for animal in sistema.animales:
        print(f"  -> {animal.codigo}: {animal.nombre} ({type(animal).__name__})")

    # Buscar el primero de la lista
    primer_codigo = sistema.animales[0].codigo
    encontrado_1 = sistema.buscar_animal_binaria(primer_codigo)
    print(f"\nBuscando el primer código ({primer_codigo}):", encontrada_resultado(encontrado_1))

    # Buscar el último de la lista
    ultimo_codigo = sistema.animales[-1].codigo
    encontrado_2 = sistema.buscar_animal_binaria(ultimo_codigo)
    print(f"Buscando el último código ({ultimo_codigo}):", encontrada_resultado(encontrado_2))

    # Buscar uno que no exista
    inexistente = "ZOO-999"
    encontrado_3 = sistema.buscar_animal_binaria(inexistente)
    print(f"Buscando un código inexistente ({inexistente}):", encontrada_resultado(encontrado_3))
    print("-" * 50)

def encontrada_resultado(animal):
    if animal:
        return f"¡Encontrado! -> {animal.nombre} ({type(animal).__name__})"
    return "None (No se encuentra en el sistema)"

if __name__ == "__main__":
    main()