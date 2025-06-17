# modelo/historiaclinica.py

class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return self.__turnos.copy()

    def obtener_recetas(self):
        return self.__recetas.copy()

    def __str__(self):
        texto = f"Historia Clínica de {self.__paciente}:\n\nTurnos:\n"
        for turno in self.__turnos:
            texto += f"- {turno}\n"
        texto += "\nRecetas:\n"
        for receta in self.__recetas:
            texto += f"- {receta}\n"
        return texto

 
