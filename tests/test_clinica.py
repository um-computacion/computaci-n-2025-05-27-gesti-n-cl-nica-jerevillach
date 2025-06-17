import unittest
from modelo.paciente import Paciente
from modelo.clinica import Clinica

class TestClinica(unittest.TestCase):
    def test_agregar_paciente(self):
        clinica = Clinica()
        paciente = Paciente("Juan Pérez", "12345678", "01/01/2000")
        clinica.agregar_paciente(paciente)
        self.assertIn(paciente, clinica.obtener_pacientes())

if __name__ == "__main__":
    unittest.main()
