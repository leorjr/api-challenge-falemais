# Fazendo a importação da variável app declarada no __init__.py
from app import create_app

# Retornando o test client do nosso app


def app_client():
    app = create_app()
    return app.test_client()


def test_status_code_rota_home():
    # Pegando o retorno da nossa função app_client()
    client = app_client()

    # Pegando a resposta da requisição na rota "/"
    response = client.get("/")

    # Testando se o status HTTP do retorno é igual ao esperado
    assert response.status_code == 200, "Status incorreto"


def test_json_response_rota_home():
    client = app_client()
    response = client.get("/")

    # Resposta esperada
    expected_dict = {
        "tarifacao": [
            {"id": 1, "origem": "11", "destino": "16", "minuto": 1.9},
            {"id": 2, "origem": "16", "destino": "11", "minuto": 2.9},
            {"id": 3, "origem": "11", "destino": "17", "minuto": 1.7},
            {"id": 4, "origem": "17", "destino": "11", "minuto": 2.7},
            {"id": 5, "origem": "11", "destino": "18", "minuto": 0.9},
            {"id": 6, "origem": "18", "destino": "11", "minuto": 1.9}
        ],
        "planos": [
            {"id": 1, "nome": "FaleMais 30", "minutos": 30},
            {"id": 2, "nome": "FaleMais 60", "minutos": 60},
            {"id": 3, "nome": "FaleMais 120", "minutos": 120}
        ]
    }

    # Testando se o retorno é um dicionário
    assert type(response.get_json()) is dict, "Não retornou dicionário"

    # Testando se o dicionário retornado é igual ao esperado
    assert response.get_json() == expected_dict, "Retorno incorreto"
