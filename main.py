"""
Módulo main.py
Punto de entrada del proyecto. Menú interactivo por consola para
gestionar tickets de soporte técnico y chequear la salud del sistema.
"""

from sistema_tickets import SistemaTickets
from monitor_sistema import chequear_salud
from ticket import Ticket

# Datos de contacto del desarrollador/soporte (editar con los datos reales)
CONTACTO_SOPORTE = {
    "nombre": "Manuel Martin",
    "email": "manumartin27.55@gmail.com",
    "github": "https://github.com/manumartin27",
}


def mostrar_menu():
    print("\n=== Sistema de Soporte IT ===")
    print("1. Crear ticket")
    print("2. Listar tickets")
    print("3. Cambiar estado de un ticket")
    print("4. Reporte de tickets pendientes por prioridad")
    print("5. Chequear salud del sistema")
    print("6. Ayuda")
    print("7. Salir")


def pedir_texto(mensaje, permitir_solo_numeros=True):
    """Pide un texto no vacío. Repite hasta que sea válido."""
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("Este campo no puede quedar vacío.")
            continue
        if not permitir_solo_numeros and texto.isdigit():
            print("Ingresá una descripción con texto, no solo números.")
            continue
        return texto


def elegir_opcion(titulo, opciones, defecto=None):
    """Pide elegir una opción por número o por nombre. Repite hasta que sea válida."""
    while True:
        print(f"{titulo}:")
        for i, opcion in enumerate(opciones, start=1):
            print(f"  {i}. {opcion}")
        sufijo = f" [{defecto}]" if defecto else ""
        entrada = input(f"Elegí por número o nombre{sufijo}: ").strip().lower()
        if not entrada and defecto:
            return defecto
        if entrada.isdigit() and 1 <= int(entrada) <= len(opciones):
            return opciones[int(entrada) - 1]
        if entrada in opciones:
            return entrada
        print("Opción inválida, intentá de nuevo.")


def crear_ticket(sistema):
    usuario = pedir_texto("Usuario/puesto de trabajo: ")
    problema = pedir_texto("Descripción del problema: ", permitir_solo_numeros=False)
    prioridad = elegir_opcion("Prioridad", Ticket.PRIORIDADES_VALIDAS, defecto="media")
    ticket_id = sistema.crear_ticket(usuario, problema, prioridad)
    print(f"Ticket #{ticket_id} creado.")


def listar_tickets(sistema):
    filas = sistema.listar_tickets()
    if not filas:
        print("\nNo hay tickets cargados todavía. Usá la opción 1 para crear el primero.")
        return
    print("\n--- Tickets ---")
    for fila in filas:
        id_t, usuario, problema, prioridad, estado, fecha = fila
        print(f"#{id_t} | {usuario} | {problema} | prioridad={prioridad} | estado={estado} | {fecha}")


def cambiar_estado(sistema):
    try:
        ticket_id = int(input("ID del ticket: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    nuevo_estado = elegir_opcion("Nuevo estado", Ticket.ESTADOS_VALIDOS)
    if sistema.cambiar_estado(ticket_id, nuevo_estado):
        print(f"Ticket #{ticket_id} actualizado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró el ticket #{ticket_id}.")


def reporte(sistema):
    resultado = sistema.reporte_por_prioridad()
    if not resultado:
        print("\nNo hay tickets pendientes (no hay tickets cargados, o todos están resueltos).")
        return
    print("\n--- Tickets pendientes por prioridad ---")
    for prioridad, cantidad in resultado.items():
        print(f"  {prioridad}: {cantidad}")


def chequeo_sistema():
    resultado = chequear_salud()
    if "error" in resultado:
        print("\n" + resultado["error"])
        return
    print("\n--- Salud del sistema ---")
    print(f"CPU: {resultado['cpu_percent']}%")
    print(f"Memoria: {resultado['memoria_percent']}%")
    print(f"Disco: {resultado['disco_percent']}%")
    if resultado["alertas"]:
        for alerta in resultado["alertas"]:
            print(f"⚠️  {alerta}")
    else:
        print("Sin alertas, todo dentro de rangos normales.")


def mostrar_ayuda():
    print("\n=== Ayuda ===")
    print("1. Crear ticket: registra un problema nuevo. Te pide el usuario o puesto")
    print("   afectado, una descripción (no puede estar vacía ni ser solo números) y la")
    print("   prioridad: 1=baja, 2=media, 3=alta (Enter = media).")
    print("2. Listar tickets: muestra todos los tickets cargados con su estado.")
    print("3. Cambiar estado: pide el ID del ticket y el nuevo estado:")
    print("   1=abierto, 2=en progreso, 3=resuelto (también podés escribir el nombre).")
    print("4. Reporte: cuenta los tickets pendientes (no resueltos) por prioridad.")
    print("5. Chequear salud del sistema: muestra el uso de CPU, memoria y disco, y")
    print("   avisa si alguno supera el 85%.")
    print("7. Salir: cierra el programa. Los tickets quedan guardados.")
    print("\n¿Dudas o problemas? Contactá al desarrollador:")
    print(f"  Nombre: {CONTACTO_SOPORTE['nombre']}")
    print(f"  Email:  {CONTACTO_SOPORTE['email']}")
    print(f"  GitHub: {CONTACTO_SOPORTE['github']}")


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
            mostrar_ayuda()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
