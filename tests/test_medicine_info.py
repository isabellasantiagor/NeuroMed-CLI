from app.medicine_info import search_medicine_info


class FakeResponse:
    status_code = 200

    def json(self):
        return {
            "results": [
                {
                    "purpose": [
                        "Pain reliever"
                    ]
                }
            ]
        }


def test_search_medicine_info_success(monkeypatch):
    """
    Testa se a integração com a API
    retorna informações corretamente.
    """

    # Simula resposta da API
    def fake_get(*args, **kwargs):
        return FakeResponse()

    # Substitui requests.get pelo fake_get
    monkeypatch.setattr(
        "app.medicine_info.requests.get",
        fake_get
    )

    result = search_medicine_info("Tylenol")

    assert result is not None
    assert result["name"] == "Tylenol"
    assert result["purpose"] == "Pain reliever"
    assert result["source"] == "OpenFDA"


def test_search_medicine_info_api_error(monkeypatch):
    """
    Testa comportamento quando a API falha.
    """

    class ErrorResponse:
        status_code = 500

    def fake_get(*args, **kwargs):
        return ErrorResponse()

    monkeypatch.setattr(
        "app.medicine_info.requests.get",
        fake_get
    )

    result = search_medicine_info("Tylenol")

    assert result is None