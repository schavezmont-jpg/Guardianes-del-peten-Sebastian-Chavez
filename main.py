from sistema_monitoreo import SistemaMonitoreo
from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano
from mono_arana import MonoArana
from zona import Zona

def main():
    sistema = SistemaMonitoreo()

    print("==================================================")
    print("   GUARDIANES DEL PETÉN - RECURSIVIDAD (E5)")
    print("==================================================\n")

    # 1. Instanciar animales
    balam = Jaguar("JAG-001", "Balam", 150.5)
    tziquin = Tapir("TAP-001", "Tziquin", 250.0)
    scarlet = GuacamayaRoja("GUA-001", "Scarlet", 90.0)
    sobek = CocodriloDePantano("COC-001", "Sobek", 3.5)
    kaan = MonoArana("MON-001", "Kaan", 80.0)

    sistema.animales.extend([balam, tziquin, scarlet, sobek, kaan])

    # 2. Armar un mapa de al menos tres niveles (Reserva -> Sector -> Aguada) y al menos 6 zonas en total
    reserva = Zona("Reserva Biosfera Maya", "Zona Principal de Conservación")
    
    sector_norte = Zona("Sector Norte", "Área de selva alta")
    aguada_el_tigre = Zona("Aguada El Tigre", "Fuente de agua permanente")
    
    sector_sur = Zona("Sector Sur", "Área de humedales y sabana")
    aguada_caimanes = Zona("Aguada Caimanes", "Pantano principal")
    
    zona_este = Zona("Sector Este", "Zona de amortiguamiento")

    # Construir la jerarquía (Árbol)
    aguada_el_tigre.ubicar(balam)          # Nivel más profundo
    sector_norte.agregar_subzona(aguada_el_tigre)
    sector_norte.ubicar(scarlet)
    
    reserva.agregar_subzona(sector_norte)

    aguada_caimanes.ubicar(sobek)          # Nivel más profundo
    sector_sur.agregar_subzona(aguada_caimanes)
    sector_sur.ubicar(tziquin)
    
    reserva.agregar_subzona(sector_sur)
    
    reserva.ubicar(kaan)                   # Animal en el nivel principal
    reserva.agregar_subzona(zona_este)     # Sexta zona para cumplir con el mínimo

    sistema.zonas.append(reserva)

    # 3. Imprimir el mapa completo con mostrar()
    print("--- 1. MAPA COMPLETO DE ZONAS (Recursivo) ---")
    reserva.mostrar()
    print("-" * 50)

    # 4. Imprimir cuántos animales hay en toda la reserva y en una zona que tenga sectores
    print("\n--- 2. CONTEO RECURSIVO DE ANIMALES ---")
    total_reserva = sistema.contar_animales()
    print(f"Total de animales en toda la reserva: {total_reserva}")
    
    total_sector_norte = sector_norte.contar_animales()
    print(f"Total de animales en el 'Sector Norte' (y sus subzonas): {total_sector_norte}")
    print("-" * 50)

    # 5. Buscar tres sectores: uno del nivel más profundo, uno de primer nivel y uno que no exista
    print("\n--- 3. BÚSQUEDA RECURSIVA DE SECTORES ---")
    
    profundo = sistema.buscar_sector("Aguada El Tigre")
    print(f"Buscando sector profundo ('Aguada El Tigre'):", resultado_sector(profundo))

    primer_nivel = sistema.buscar_sector("Sector Norte")
    print(f"Buscando sector de primer nivel ('Sector Norte'):", resultado_sector(primer_nivel))

    inexistente = sistema.buscar_sector("Volcán de Fuego")
    print(f"Buscando sector inexistente ('Volcán de Fuego'):", resultado_sector(inexistente))
    print("-" * 50)

def resultado_sector(sector):
    if sector:
        return f"¡Encontrado! -> {sector.nombre} ({sector.descripcion})"
    return "None (No se encuentra en el sistema)"

if __name__ == "__main__":
    main()