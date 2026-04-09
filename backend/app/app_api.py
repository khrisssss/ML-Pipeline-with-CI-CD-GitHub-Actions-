from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path


app = FastAPI(title="Iris Classification API")


class Items(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float


@app.get("/")
def root():
    return {"status": "OK"}

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "ml" / "model.pkl"



model = joblib.load(MODEL_PATH)


@app.post("/predict")
def predict(item: Items):
    features = [[
        item.SepalLengthCm,
        item.SepalWidthCm,
        item.PetalLengthCm,
        item.PetalWidthCm
    ]]

    prediction = model.predict(features)[0]

    return {"prediction": prediction}
