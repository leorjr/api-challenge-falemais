import json


def load_db():
    with open("./database/db.json", "r") as file:
        data = json.load(file)

    return data


def calculate(plano_escolhido, tarifacao, dados_request):

    saldo_restante = plano_escolhido["minutos"] - dados_request["tempo"]

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
