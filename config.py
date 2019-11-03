import yaml


class Config(dict):
    
    def __init__(self, filepath):
        with open(filepath) as f:
            super().__init__(yaml.load(f, Loader=yaml.FullLoader))
