"""
Módulo main.py
Punto de entrada del proyecto. Menú interactivo por consola para
gestionar tickets de soporte técnico y chequear la salud del sistema.
"""

from sistema_tickets import SistemaTickets
from monitor_sistema import chequear_salud


def mostrar_menu():
    print("\n=== Sistema de Soporte IT ===")
    print("1. Crear ticket")
    print("2. Listar tickets")
    print("3. Cambiar estado de un ticket")
    print("4. Reporte de tickets pendientes por prioridad")
    print("5. Chequear salud del sistema")
    print("6. Salir")


def crear_ticket(sistema):
    usuario = input("Usuario/puesto de trabajo: ").strip()
    problema = input("Descripción del problema: ").strip()
    prioridad = input("Prioridad (baja/media/alta) [media]: ").strip().lower() or "media"
    if prioridad not in ("baja", "media", "alta"):
        print("Prioridad inválida, se usará 'media'.")
        prioridad = "media"
    ticket_id = sistema.crear_ticket(usuario, problema, prioridad)
    print(f"Ticket #{ticket_id} creado.")


def listar_tickets(sistema):
    filas = sistema.listar_tickets()
    if not filas:
        print("No hay tickets cargados.")
        return
    for fila in filas:
        id_t, usuario, problema, prioridad, estado, fecha = fila
        print(f"#{id_t} | {usuario} | {problema} | prioridad={prioridad} | estado={estado} | {fecha}")


def cambiar_estado(sistema):
    try:
        ticket_id = int(input("ID del ticket: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    nuevo_estado = input("Nuevo estado (abierto/en progreso/resuelto): ").strip().lower()
    if nuevo_estado not in ("abierto", "en progreso", "resuelto"):
        print("Estado inválido.")
        return
    if sistema.cambiar_estado(ticket_id, nuevo_estado):
        print(f"Ticket #{ticket_id} actualizado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró el ticket #{ticket_id}.")


def reporte(sistema):
    resultado = sistema.reporte_por_prioridad()
    if not resultado:
        print("No hay tickets pendientes.")
        return
    print("Tickets pendientes por prioridad:")
    for prioridad, cantidad in resultado.items():
        print(f"  {prioridad}: {cantidad}")


def chequeo_sistema():
    resultado = chequear_salud()
    if "error" in resultado:
        print(resultado["error"])
        return
    print(f"CPU: {resultado['cpu_percent']}%")
    print(f"Memoria: {resultado['memoria_percent']}%")
    print(f"Disco: {resultado['disco_percent']}%")
    if resultado["alertas"]:
        for alerta in resultado["alertas"]:
            print(f"⚠️  {alerta}")
    else:
        print("Sin alertas, todo dentro de rangos normales.")


def main():
    sistema = SistemaTickets()
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()
        if opcion == "1":
            crear_ticket(sistema)
        elif opcion == "2":
            listar_tickets(sistema)
        elif opcion == "3":
            cambiar_estado(sistema)
        elif opcion == "4":
            reporte(sistema)
        elif opcion == "5":
            chequeo_sistema()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
