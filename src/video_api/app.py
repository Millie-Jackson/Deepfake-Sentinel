from fastapi import FastAPI
from .model import load_model, predict

app = FastAPI()
model = load_model()

@app.post("/predict")


def predict_video(data: dict):
    # TODO: extract frame(s), call predict(model, ...)
    return {"prediction": predict(model, data)}
