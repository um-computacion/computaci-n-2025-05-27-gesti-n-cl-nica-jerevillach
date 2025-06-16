# modelo/receta.py

from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        return f"{medicamentos_str} - Emitida el: {self.__fecha.strftime('%d/%m/%Y')}"
