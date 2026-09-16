"""
Módulo ticket.py
Define la clase Ticket, que representa un ticket de soporte técnico
(problema reportado por un usuario/puesto de trabajo, con prioridad y estado).
"""

from datetime import datetime


class Ticket:
    """Representa un ticket de soporte técnico."""

    ESTADOS_VALIDOS = ("abierto", "en progreso", "resuelto")
    PRIORIDADES_VALIDAS = ("baja", "media", "alta")

    def __init__(self, id_ticket, usuario, problema, prioridad="media", estado="abierto"):
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: {estado}")

        self.id_ticket = id_ticket
        self.usuario = usuario
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado
        self.fecha_creacion = datetime.now().isoformat(timespec="seconds")

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: {nuevo_estado}")
        self.estado = nuevo_estado

    def __repr__(self):
        return f"Ticket(#{self.id_ticket}, {self.usuario!r}, {self.prioridad}, {self.estado})"
