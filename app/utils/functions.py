import json


def load_db():
    with open("./database/db.json", "r") as file:
        data = json.load(file)

    return data
