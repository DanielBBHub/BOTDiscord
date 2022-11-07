from .calendario import Calendario
import pytest

class TestCalendario:
    @pytest.fixture
    def get_calendario(self):
        calendario = Calendario()
        calendario.anyadir_examen("2022-11-06", "Redes", "Teoria")
        return calendario

    def test_crear_examen(self):
        self.calendario = Calendario()
        self.calendario.anyadir_examen("2022-11-06", "Redes", "Teoria")
        assert self.calendario.examenes["Redes"].tipo == "Teoria"
    
    def test_anyadir_miembro(self, get_calendario):
        get_calendario.anyadir_miembro("Redes","301672737246806018")
        assert get_calendario.examenes["Redes"].alumnos[0] == 301672737246806018
