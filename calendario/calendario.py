
from .examen import Examen
import discord

class Calendario(discord.ScheduledEvent):

    """ Para la clase calendario se necesitara estructuras de datos para albergar:
        - Fecha examen
        - Examen
       """

    def __init__(self):
        
        # Cargar archivo con el calendario

        # Cargar los datos del archivo

        # fecha: Examen
        self.examenes = dict()


    def anyadir_examen(self, fecha, nombre_asignatura, tipo,*, alumnos=""):
        alumnos_examen = set()
        for alumno in alumnos:
            alumnos_examen.add(alumno)

        examen = Examen(fecha, nombre_asignatura, tipo, alumnos = alumnos_examen )
        self.examenes.setdefault(nombre_asignatura, examen)
        
        for llave, valor in self.examenes.items():
            print("\nExamenes inscrito: ")
            print(llave)
            print(":")
            print(valor)

    """ async def crear_evento(self):
        await self.eventos.start(status=discord.EventStatus.active) """
        
    



