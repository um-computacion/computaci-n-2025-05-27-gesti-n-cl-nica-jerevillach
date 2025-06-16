# modelo/medico.py

from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str):
        dia = dia.lower()
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self):
        especialidades = "\n  - ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre} (Matrícula: {self.__matricula})\n  - {especialidades}"

