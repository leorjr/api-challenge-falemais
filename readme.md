# API REST FaleMais

O objetivo desta API é fazer um comparativo, de forma fácil e rápida,
para o nosso lead, trazendo as informações de custo de quanto o mesmo
gastaria sem ser nosso cliente e, quanto que o mesmo gastaria sendo nosso
cliente, adquirindo e utilizando um de nossos planos.

## Features

- Listar todas as informações (planos e tarifas);
- Listar apenas planos;
- Listar apenas tarifas;
- Realizar uma simulação de uso, trazendo um comparativo de valores entre uso do plano e o não uso;

## Tech

As principais tecnologias que foram utilizadas neste projeto são:

- Python3;
- Flask;

## Installation

Para rodar este projeto localmente, você deverá entrar na pasta do mesmo:

```
cd api-challenge
```

Dentro da pasta, você deverá criar uma variável de ambiente (venv) utilizando os seguintes comandos:

```
python -m venv venv
```

Em seguida, deverá ativar o ambiente criado:

```
source venv/bin/activate
```

Em seguida, deverá instalar as dependencias do projeto com o seguinte comando:

```
pip install -r requirements.txt
```

Por fim, para rodar o projeto localmente, deverá dar o seguinte comando:

```
flask run
```

No terminal, será informado o endereço onde você deverá usar no navegador. Geralmente, é o endereço http://127.0.0.1:5000/

## ENDPOINTS

Abaixo temos os endpoints para uso desta API:

| Method | EndPoint           | Response                                                                                  | Request Data                                                                                                                         |
| ------ | ------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| GET    | /                  | Será retornado todos os planos e todas as tarifações                                      | --                                                                                                                                   |
| GET    | /plans             | Será retornado todos os planos e suas informações                                         | --                                                                                                                                   |
| GET    | /pricing           | Será retornado todos os preços de uso sem os planos                                       | --                                                                                                                                   |
| POST   | /calculate-pricing | Será retornado um cálculo comparativo com as informações de uso com o plano e sem o plano | Deverá enviar um objeto com as chaves origem, destino, tempo, plano. Ex.: {"origem":"x", "destino": "y", "tempo": "w", "plano": "z"} |
