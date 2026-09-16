"""
Módulo sistema_tickets.py
Define la clase SistemaTickets, que gestiona la persistencia de
tickets de soporte en una base de datos SQLite: creación, cambio
de estado, listado y reporte por prioridad.
"""

import sqlite3
from datetime import datetime


class SistemaTickets:
    """Gestiona el ciclo de vida de los tickets de soporte técnico."""

    def __init__(self, db_path="tickets.db"):
        self.db_path = db_path
        self._inicializar_db()

    def _inicializar_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                problema TEXT,
                prioridad TEXT,
                estado TEXT,
                fecha_creacion TEXT
            )
            """
        )
        conn.commit()
        conn.close()

    def crear_ticket(self, usuario, problema, prioridad="media"):
        fecha = datetime.now().isoformat(timespec="seconds")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tickets (usuario, problema, prioridad, estado, fecha_creacion)
            VALUES (?, ?, ?, ?, ?)
            """,
            (usuario, problema, prioridad, "abierto", fecha),
        )
        conn.commit()
        ticket_id = cursor.lastrowid
        conn.close()
        return ticket_id

    def cambiar_estado(self, ticket_id, nuevo_estado):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE tickets SET estado = ? WHERE id = ?", (nuevo_estado, ticket_id))
        conn.commit()
        filas_afectadas = cursor.rowcount
        conn.close()
        return filas_afectadas > 0

    def listar_tickets(self, estado=None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        if estado:
            cursor.execute(
                "SELECT id, usuario, problema, prioridad, estado, fecha_creacion "
                "FROM tickets WHERE estado = ?",
                (estado,),
            )
        else:
            cursor.execute(
                "SELECT id, usuario, problema, prioridad, estado, fecha_creacion FROM tickets"
            )
        filas = cursor.fetchall()
        conn.close()
        return filas

    def reporte_por_prioridad(self):
        """Cuenta los tickets no resueltos, agrupados por prioridad."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT prioridad, COUNT(*)
            FROM tickets
            WHERE estado != 'resuelto'
            GROUP BY prioridad
            """
        )
        resultado = dict(cursor.fetchall())
        conn.close()
        return resultado
