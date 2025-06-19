import yaml


def load_config(path="config.yaml"):
    with open(path) as f:
        temp = yaml.safe_load(f)
    return temp
