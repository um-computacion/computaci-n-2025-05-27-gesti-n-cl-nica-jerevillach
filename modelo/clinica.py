# clinica.py
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historiaclinica import HistoriaClinica
from modelo.excepciones import *

from datetime import datetime

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    def agregar_paciente(self, paciente: Paciente):
        if paciente.obtener_dni() in self.__pacientes:
            raise Exception("El paciente ya está registrado.")
        self.__pacientes[paciente.obtener_dni()] = paciente
        self.__historias_clinicas[paciente.obtener_dni()] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        if medico.obtener_matricula() in self.__medicos:
            raise Exception("El médico ya está registrado.")
        self.__medicos[medico.obtener_matricula()] = medico

    def obtener_pacientes(self):
        return list(self.__pacientes.values())

    def obtener_medicos(self):
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(matricula)
        return self.__medicos[matricula]

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.__medicos[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)

        if especialidad_disponible != especialidad:
            raise EspecialidadNoDisponibleException(especialidad, dia_semana)

        turno = Turno(self.__pacientes[dni], medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        if not medicamentos:
            raise RecetaInvalidaException("Debe ingresar al menos un medicamento.")
        receta = Receta(self.__pacientes[dni], self.__medicos[matricula], medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_turnos(self):
        return self.__turnos.copy()

    def obtener_historia_clinica(self, dni: str):
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(dni)

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(matricula)

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException()

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str):
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad: str, dia_semana: str):
        if medico.obtener_especialidad_para_dia(dia_semana) != especialidad:
            raise EspecialidadNoDisponibleException(especialidad, dia_semana)


