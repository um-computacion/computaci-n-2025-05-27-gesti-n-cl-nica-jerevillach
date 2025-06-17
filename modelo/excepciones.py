# modelo/excepciones.py

class PacienteNoEncontradoException(Exception):
    def __init__(self, dni):
        super().__init__(f"No se encontró un paciente con DNI {dni}.")

class MedicoNoDisponibleException(Exception):
    def __init__(self, mensaje="El médico no está disponible para la especialidad o el día indicado."):
        super().__init__(mensaje)

class TurnoOcupadoException(Exception):
    def __init__(self):
        super().__init__("El turno ya está ocupado por otro paciente.")

class RecetaInvalidaException(Exception):
    def __init__(self, mensaje="Receta inválida. Verifique los datos ingresados."):
        super().__init__(mensaje)

class MedicoNoEncontradoException(Exception):
    def __init__(self, matricula):
        super().__init__(f"No se encontró un médico con matrícula {matricula}.")

class EspecialidadNoDisponibleException(Exception):
    def __init__(self, especialidad, dia):
        super().__init__(f"La especialidad '{especialidad}' no está disponible el día {dia}.")
