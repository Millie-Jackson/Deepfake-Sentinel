from fastapi import FastAPI
from .model import load_model, predict

app = FastAPI()
model = load_model()

@app.post("/predict")


def predict_audio(data: dict):
    # TODO: extract audio snippet, call predict(model, …)
    return {"prediction": predict(model, data)}
