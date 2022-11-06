from .calendario import Calendario

class TestCalendario:
    def test_crear_examen(self):
        calendario = Calendario()
        calendario.anyadir_examen("2022-11-06", "Redes", "Teoria", "3º")
        assert calendario.examenes["2022-11-06"].nombre_asignatura == "Redes"