
class Examen:
    """
    Para la clase examen se necesitara estructuras de datos para albergar:
        - Nombre asignatura
        - Tipo (teoria / practica)
        - Curso
        - Alumnos a examinar
    
    """
    def __init__(self, nombre_asignatura, tipo, curso, *, alumnos=""):
        self.nombre_asignatura = nombre_asignatura
        self.tipo = tipo
        self.curso = curso
        self.alumnos = set()
        for alumno in alumnos:
            alumnos.add(alumno)


    
    def toString(self):
            return f"""
            Nombre asignatura: {1},
            Tipo: {2},             
            Curso: {3},            
            Alumnos: {4}
            """.format(self.nombre_asignatura, self.tipo, self.curso, self.alumnos)
        
    