import json


class Configurator:

    def __init__(self):
        with open('config.json') as config_file:
            self.config = json.load(fp=config_file)
