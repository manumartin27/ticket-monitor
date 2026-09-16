# Soporte IT — Sistema de Tickets y Chequeo de Salud

Simulador en Python de dos herramientas típicas de un puesto de soporte
técnico de nivel 1: un **sistema de tickets** para registrar y hacer
seguimiento de incidencias reportadas por usuarios, y un **chequeo
rápido de salud** de un equipo o servidor (CPU, memoria, disco).

## ¿Por qué este proyecto?

Pensado como pieza de portfolio para roles de soporte técnico
informático: asistencia a puestos de trabajo y servidores, y
resolución/seguimiento de incidencias. Simula el flujo real de un
área de soporte: **reportar problema → registrar ticket → priorizar
→ resolver → diagnosticar el equipo**.

## Estructura del proyecto

```
soporte-it/
├── ticket.py            # Clase Ticket
├── sistema_tickets.py   # Clase SistemaTickets: persiste tickets en SQLite, genera reportes
├── monitor_sistema.py   # Chequeo de salud del sistema (CPU/memoria/disco) con psutil
├── main.py              # Punto de entrada: menú interactivo por consola
├── requirements.txt
└── README.md
```

## Conceptos de Python que muestra

- Programación orientada a objetos (clase `Ticket`)
- Persistencia con `sqlite3` (módulo estándar)
- Manejo de dependencias externas de forma segura (`psutil`, con
  fallback si no está instalado)
- Menú interactivo por consola con `input()`
- Separación de responsabilidades en distintos módulos

## Requisitos

- Python 3.10+
- `psutil` (solo para el chequeo de salud del sistema — ver
  `requirements.txt`). El resto del programa (tickets) funciona sin
  dependencias externas.

## Instalación

```bash
pip install -r requirements.txt
```

## Cómo ejecutarlo

```bash
python main.py
```

Vas a ver un menú con opciones para crear tickets, listarlos, cambiar
su estado, ver un reporte de pendientes por prioridad, y chequear la
salud del sistema. Los tickets quedan guardados en `tickets.db`
(SQLite), generado automáticamente en la primera ejecución.

## Posibles mejoras a futuro

- Exportar el reporte de tickets a CSV
- Agregar un campo de "técnico asignado" por ticket
- Alertas automáticas por email/Slack cuando un ticket de prioridad
  alta lleva mucho tiempo sin resolverse
- Reemplazar el menú de consola por una API simple con `Flask`
- Tests con `unittest` o `pytest`
