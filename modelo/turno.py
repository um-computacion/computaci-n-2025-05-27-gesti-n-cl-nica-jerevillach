# turno.py

from datetime import datetime

class Turno:
    """Representa el turno de un paciente con un médico."""
    
    def __init__(self, id, paciente, medico, fecha_hora):
        self.id = id
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    def __str__(self):
        return f"Turno(id={self.id}, paciente='{self.paciente}', médico='{self.medico}', fecha_hora='{self.fecha_hora}')"

# Ejemplo de uso:
if __name__ == "__main__":
    from modelo.paciente import Paciente
    from modelo.medico import Medico
    
    paciente = Paciente(1, "Juan", "Perez", "12345678", "1990-05-04")
    medico = Medico(1, "Carlos", "Lopez", "MAT1234", "Pediatría")
    turno = Turno(1, paciente, medico, datetime(2024, 6, 16, 10, 30))
    print(turno)
