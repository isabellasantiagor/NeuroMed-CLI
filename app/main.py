from app.medication import MedicationManager
from app.medicine_info import search_medicine_info


def input_with_back(message):
    value = input(message)
    if value == "0":
        return None
    return value


def main():
    manager = MedicationManager()

    # Menu inicial
    while True:
        print("\n== NeuroMed CLI ==")
        print("1 - Adicionar medicamento")
        print("2 - Listar medicamentos cadastrados")
        print("3 - Remover medicamento cadastrado")
        print("4 - Sair")
        print("5 - Buscar informações de medicamento")

        choice = input("Escolha: ")

        # Escolha 01
        if choice == "1":
            print("Digite 0 a qualquer momento para voltar ao menu principal")

            name = input_with_back("Nome do medicamento: ")
            if name is None:
                continue

            time = input_with_back("Horário (HH:MM): ")
            if time is None:
                continue

            dosage = input_with_back("Dosagem (mg): ")
            if dosage is None:
                continue

            try:
                manager.add_medication(name, time, dosage)
                print("Medicamento adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        # Escolha 02
        elif choice == "2":
            print("Digite 0 e pressione ENTER para voltar ao menu principal")

            meds = manager.list_medications()

            if not meds:
                print("Nenhum medicamento cadastrado")
            else:
                print("\nMedicamentos cadastrados:")
                for m in meds:
                    print(f"- {m['name']} | {m['dosage']}mg | às {m['time']}")

            back = input()
            if back == "0":
                continue

        # Escolha 03
        elif choice == "3":
            print("Digite 0 para voltar ao menu principal")

            name = input_with_back("Nome para remover: ")
            if name is None:
                continue

            try:
                manager.remove_medication(name)
                print("Medicamento removido com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        # Escolha 05
        elif choice == "5":
            print("Digite 0 para voltar ao menu principal")

            medicine_name = input_with_back("Nome do medicamento: ")

            if medicine_name is None:
                continue

            info = search_medicine_info(medicine_name)

            if info:
                print("\nInformações encontradas:")
                print(f"Medicamento pesquisado: {info['name']}")
                print(f"Finalidade: {info['purpose']}")
                print(f"Fonte: {info['source']}")

                print(
                    "\nAviso: informação apenas consultiva. "
                    "Não substitui orientação médica ou farmacêutica."
                )

            else:
                print(
                    "Nenhuma informação encontrada para este medicamento. "
                    "Tente nomes internacionais como Tylenol, Advil ou Aspirin."
                )
        # Escolha 04
        elif choice == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente")


if __name__ == "__main__":
    main()