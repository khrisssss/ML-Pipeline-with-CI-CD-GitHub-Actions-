from ..app.app_api import app
from fastapi.testclient import TestClient

test_client = TestClient(app)

iris_setosa = {
    "SepalLengthCm": 4.9,
    "SepalWidthCm": 3.0,
    "PetalLengthCm": 1.4,
    "PetalWidthCm": 0.2
}

def test_model_predict():
    response =  test_client.post("/predict", json=iris_setosa)

    print(response.json())

    assert response.status_code == 200
    assert "prediction" in response.json()
    