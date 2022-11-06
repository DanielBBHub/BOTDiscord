
from .examen import Examen

class Calendario:

    """ Para la clase calendario se necesitara estructuras de datos para albergar:
        - Fecha examen
        - Examen
       """

    def __init__(self):
        
        # Cargar archivo con el calendario

        # Cargar los datos del archivo

        # fecha: Examen
        self.examenes = dict()



    def anyadir_examen(self, fecha, nombre_asignatura, tipo, curso, *, alumnos=""):
        alumnos_examen = set()
        for alumno in alumnos:
            alumnos_examen.add(alumno)

        examen = Examen(nombre_asignatura, tipo, curso, alumnos = alumnos_examen )
        examen.toString()
        self.examenes.setdefault(fecha, examen)
        print(str(self.examenes))


