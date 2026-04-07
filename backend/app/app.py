from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK"}

@app.post("/predict")
def predict():
    return 