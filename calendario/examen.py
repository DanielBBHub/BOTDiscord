
class Examen:
    """
    Para la clase examen se necesitara estructuras de datos para albergar:
        - Nombre asignatura
        - Tipo (teoria / practica)
        - Curso
        - Alumnos a examinar
    
    """
    def __init__(self,fecha, nombre_asignatura, tipo, *, alumnos=""):
        self.nombre_asignatura = nombre_asignatura
        self.tipo = tipo
        self.fecha = fecha
        self.alumnos = set()
        for alumno in alumnos:
            alumnos.add(alumno)


    
    def anyadir_alumno(self, alumno):
        self.alumnos.add(alumno)

    def __str__(self):
        
        return f"""
            Nombre asignatura: {self.nombre_asignatura},
            Tipo: {self.tipo},             
            Alumnos: {self.alumnos}
            """
    