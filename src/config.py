import json


def load_config(path):

    with open(path) as file:

        return json.load(file)