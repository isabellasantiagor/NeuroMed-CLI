import requests


def search_medicine_info(medicine_name):
    """
    Busca informações básicas de um medicamento
    utilizando API pública.
    """

    url = (
        "https://api.fda.gov/drug/label.json"
        f"?search=openfda.brand_name:{medicine_name}&limit=1"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        results = data.get("results")

        if not results:
            return None

        medicine = results[0]

        purpose = medicine.get(
            "purpose",
            ["Informação não disponível"]
        )[0]

        return {
            "name": medicine_name,
            "purpose": purpose,
            "source": "OpenFDA"
        }

    except requests.RequestException:
        return None