# cli.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import *
from datetime import datetime

clinica = Clinica()

def menu():
    while True:
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agregar especialidad a médico")
        print("4) Agendar turno")
        print("5) Emitir receta")
        print("6) Ver historia clínica de un paciente")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

        opcion = input("Elija una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre completo del paciente: ")
                dni = input("DNI del paciente: ")
                fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
                paciente = Paciente(nombre, dni, fecha_nac)
                clinica.agregar_paciente(paciente)
                print("✅ Paciente agregado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre completo del médico: ")
                matricula = input("Matrícula profesional: ")
                medico = Medico(nombre, matricula)
                clinica.agregar_medico(medico)
                print("✅ Médico agregado correctamente.")

            elif opcion == "3":
                matricula = input("Matrícula del médico: ")
                tipo = input("Nombre de la especialidad: ")
                dias = input("Días de atención (separados por coma, en minúscula): ").split(",")
                especialidad = Especialidad(tipo, [d.strip() for d in dias])
                medico = clinica.obtener_medico_por_matricula(matricula)
                medico.agregar_especialidad(especialidad)
                print("✅ Especialidad agregada.")

            elif opcion == "4":
                dni = input("DNI del paciente: ")
                matricula = input("Matrícula del médico: ")
                especialidad = input("Especialidad deseada: ")
                fecha_str = input("Fecha y hora del turno (dd/mm/aaaa HH:MM): ")
                fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
                clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
                print("✅ Turno agendado correctamente.")

            elif opcion == "5":
                dni = input("DNI del paciente: ")
                matricula = input("Matrícula del médico: ")
                medicamentos = input("Lista de medicamentos (separados por coma): ").split(",")
                clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
                print("✅ Receta emitida correctamente.")

            elif opcion == "6":
                dni = input("DNI del paciente: ")
                historia = clinica.obtener_historia_clinica(dni)
                print(historia)

            elif opcion == "7":
                for turno in clinica.obtener_turnos():
                    print(turno)

            elif opcion == "8":
                for paciente in clinica.obtener_pacientes():
                    print(paciente)

            elif opcion == "9":
                for medico in clinica.obtener_medicos():
                    print(medico)

            elif opcion == "0":
                print("👋 Saliendo del sistema.")
                break

            else:
                print("⚠️ Opción no válida.")

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    menu()
