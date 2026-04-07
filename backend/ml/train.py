import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.sklearn.autolog()


def train():
    df = pd.read_csv("../../datas/Iris.csv")

    train, test = train_test_split(df, test_size = 0.3)
    train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]# taking the training data features
    train_y=train.Species# output of our training data
    test_X= test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data features
    test_y =test.Species   #output value of test data

    params = {
        "n_estimators": 100,
        "random_state": 45,
    }
    
    with mlflow.start_run():
        mlflow.log_params(params)

        RFC = RandomForestClassifier (**params)
        RFC.fit(train_X, train_y)

        y_pred = RFC.predict(test_X)
        accuracy = accuracy_score(test_y, y_pred)
        mlflow.log_metric("accuracy", accuracy)

        print(f"Accuracy: {accuracy}")

    joblib.dump(RFC, "model.pkl")

if __name__ == "__main__":
    train()
