import pytest
from app.medication import MedicationManager

##Manager 
@pytest.fixture
def manager(monkeypatch):
    # Mocka o load_data 
    monkeypatch.setattr("app.medication.load_data", lambda: [])

    # Mocka o save_data 
    monkeypatch.setattr("app.medication.save_data", lambda data: None)

    return MedicationManager()

#Testar adicionar o med
def test_add_medication_success(manager):
    manager.add_medication("Dipirona", "10:00", 500)

    meds = manager.list_medications()

    assert len(meds) == 1
    assert meds[0]["name"] == "Dipirona"
    assert meds[0]["time"] == "10:00"
    assert meds[0]["dosage"] == 500.0

#Testar tempo incorreto (fora do formato 24)
def test_invalid_time(manager):
    with pytest.raises(ValueError, match="Horário inválido"):
        manager.add_medication("Dipirona", "25:00", 500)

#Testar dosagem errada
def test_invalid_dosage(manager):
    with pytest.raises(ValueError, match="Dosagem deve ser um número positivo"):
        manager.add_medication("Dipirona", "10:00", -10)

#Testar medicação dup
def test_duplicate_medication(manager):
    manager.add_medication("Dipirona", "10:00", 500)

    with pytest.raises(ValueError, match="Medicamento já cadastrado"):
        manager.add_medication("dipirona", "12:00", 750)

#Testar lista
def test_list_medications(manager):
    manager.add_medication("Dipirona", "10:00", 500)
    manager.add_medication("Paracetamol", "12:00", 750)

    meds = manager.list_medications()

    assert len(meds) == 2

#Testar remover os med
def test_remove_medication_success(manager):
    manager.add_medication("Dipirona", "10:00", 500)

    manager.remove_medication("Dipirona")

    meds = manager.list_medications()
    assert meds == []

#Testar med n cadast
def test_remove_nonexistent_medication(manager):
    with pytest.raises(ValueError, match="Medicamento não encontrado"):
        manager.remove_medication("Inexistente")

#Dosagem zerada (não tomar nada??)
def test_zero_dosage_case_limit(manager):
    with pytest.raises(ValueError, match="Dosagem deve ser um número positivo"):
        manager.add_medication("Dipirona", "10:00", 0)