import json
from app.exc.home_exceptions import HomeExceptions


def load_db():
    with open("./database/db.json", "r") as file:
        data = json.load(file)

    return data


def get_tarifacao(dados_request, db):
    tarifacao = None

    for item in db["tarifacao"]:
        if (item["origem"] == str(dados_request["origem"])) and (item["destino"] == str(dados_request["destino"])):
            tarifacao = item

    return tarifacao


def get_plano_escolhido(dados_request, db):

    plano_escolhido = None

    for item in db["planos"]:
        if item["nome"] == dados_request["plano"]:
            plano_escolhido = item

    return plano_escolhido


def calculate(plano_escolhido, tarifacao, dados_request):

    try:
        saldo_restante = plano_escolhido["minutos"] - dados_request["tempo"]
    except TypeError as e:
        return {"error": "a chave tempo precisa ser valor inteiro"}

    valor_a_pagar = 0 if saldo_restante > 0 else ((
        tarifacao["minuto"] + (tarifacao["minuto"] * 0.10)) * saldo_restante) * (-1)

    valor_a_pagar_sem_plano = dados_request["tempo"] * tarifacao["minuto"]

    calculated = {
        "origem": tarifacao["origem"],
        "destino": tarifacao["destino"],
        "tempo": dados_request["tempo"],
        "plano FaleMais": dados_request["plano"],
        "com FaleMais": valor_a_pagar,
        "sem FaleMais": valor_a_pagar_sem_plano,
    }

    return calculated
