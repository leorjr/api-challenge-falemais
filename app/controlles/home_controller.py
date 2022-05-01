from flask import Flask, jsonify, request
from app.exc.home_exceptions import HomeExceptions
from app.utils import functions


def init_app(app: Flask):

    @app.get("/")
    def home():
        data = functions.load_db()

        return data

    @app.get("/planos")
    def get_planos():
        data = functions.load_db()

        return jsonify(data["planos"])

    @app.get("/tarifacao")
    def get_tarifacao():
        data = functions.load_db()

        return jsonify(data["tarifacao"])

    @app.post("/calcular")
    def calculate():

        dados_request = request.json

        required_keys = ["origem", "destino", "tempo", "plano"]

        for key in dados_request.keys():
            if key not in required_keys:
                return {"err": f"Informar apenas origem, destino, tempo e plano escolhido - chave {key} desconhecida"}

        for key in required_keys:
            if key not in dados_request.keys():
                return {"err": f"favor informar {key}"}

        db = functions.load_db()

        tarifacao = functions.get_tarifacao(dados_request, db)

        plano_escolhido = functions.get_plano_escolhido(dados_request, db)

        if plano_escolhido == None:
            return {"error": f"Plano {dados_request['plano']} não localizado em nosso portfólio"}

        response = functions.calculate(
            plano_escolhido, tarifacao, dados_request)

        return response
