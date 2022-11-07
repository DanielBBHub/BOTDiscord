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


    def anyadir_examen(self, fecha, nombre_asignatura, tipo):

        examen = Examen(fecha, nombre_asignatura, tipo)
        self.examenes.setdefault(nombre_asignatura, examen)
        
        for llave, valor in self.examenes.items():
            print("\nExamenes inscrito: ")
            print(llave)
            print(":")
            print(valor)
    
    def anyadir_miembro(self, nombre_asignatura, id_miembro):
        examen = self.examenes[nombre_asignatura]
        examen.anyadir_alumno(int(id_miembro))


    """ async def crear_evento(self):
        await self.eventos.start(status=discord.EventStatus.active) """