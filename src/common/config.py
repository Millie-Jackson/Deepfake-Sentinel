import yaml
import os

def load_config(path="config.yaml"):
  with open(path) as f:
    return yaml.safe_load(f)
