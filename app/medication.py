from datetime import datetime
from app.storage import load_data, save_data

class MedicationManager:
    def __init__(self):
        self.medications = load_data()

    def _validate_time(self, time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
        except ValueError:
            raise ValueError("Horário inválido. Use o formato HH:MM (24h)")

    def _is_duplicate(self, name):
        for med in self.medications:
            if med["name"].lower() == name.lower():
                return True
        return False

    def add_medication(self, name, time, dosage):
        ## Validação de campos obrigatórios
        if not name or not time:
            raise ValueError("Nome e horário são obrigatórios")

        ## Validação de horário
        self._validate_time(time)

        ## Impedir duplicidade
        if self._is_duplicate(name):
            raise ValueError("Medicamento já cadastrado")

        ## Validação de dosagem
        try:
            dosage = float(dosage)
            if dosage <= 0:
                raise ValueError
        except ValueError:
            raise ValueError("Dosagem deve ser um número positivo")

        ## Adiciona medicamento
        self.medications.append({
            "name": name,
            "time": time,
            "dosage": dosage
        })

        ## Salva para o json
        save_data(self.medications)

    def list_medications(self):
        return self.medications

    def remove_medication(self, name):
        for medication in self.medications:
            if medication["name"].lower() == name.lower():
                self.medications.remove(medication)

                ## Salva para o json
                save_data(self.medications)
                return

        ## Erro de não encontrar
        raise ValueError("Medicamento não encontrado")