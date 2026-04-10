This is a simple machine learning project using MLflow to train a model on the Iris dataset, applying logistic regression.

As students from Simplon, this project is part of our training. We trained a model to predict three different varieties of Iris flowers based on sepal and petal length and width (in cm).

I am proud to say that I completed this project without relying on LLMs. While there were some challenges, my colleagues were always there to support me.
I would like to thank all my teammates who helped make this project successful.

### Objective of this project is to understand how to build the CI/CD Pipeline in Github Actions and Deploy it in Azure. 

# Project Structure 
ml_pipeline/
├── backend/
│   ├── app/
│   │   └── app_api.py               # Flask API
│   │
│   ├── ml/
│   │   ├── train_notebook.ipynb     # Jupyter notebook for data exploration
│   │   └── train.py                 # Train the model with MLflow
│   │
│   ├── test/
│   │   └── test_predict.py          # Verify that the model can be loaded
│   │
│   └── Dockerfile                   # Backend Dockerfile
│
├── frontend/
│   ├── app/                         # Streamlit frontend
│   └── Dockerfile                   # Frontend Dockerfile
│
├── .gitignore
│
└── DOCUMENTATION.md       
--------------------------------------------------------------------------------------------------------

# Launching in local 

#### to launch front with streamlit
frontend
'''bash 
streamlit run app.py
'''

#### for the backend 
backend/app
''' bash 
uvicorn app_api:app 
'''

#### to launch mlflow
''' bash
mlflow ui
'''


# test 
Wen you do a test if the connection is correct make sure you are just in the folder of ml_pipeline then run 
''' bash 
pytest
'''
If you see i collected an item and its not failed then connection is good



#### to build the image of backend docker file
ml_pipeline/backend
''' bash 
docker build --no-cache -t backend .
'''  
------------------------------------------------------------------------------------------------------------

# API Docs
Endpoints 

| Method | Route      | Description                  | Request Body          | Response Example                  |
| ------ | ---------- | ---------------------------- | --------------------- | --------------------------------- |
| GET    | `/`        | Check if the API is running  | None                  | `{ "status": "ok" }`              |
| POST   | `/predict` | Predict Iris flower category | JSON input (features) | `{ "prediction": "Iris-setosa" }` |

POST /predict details 
| Field         | Type  | Description        |
| ------------- | ----- | ------------------ |
| SepalLengthCm | float | Sepal length in cm |
| SepalWidthCm  | float | Sepal width in cm  |
| PetalLengthCm | float | Petal length in cm |
| PetalWidthCm  | float | Petal width in cm  |


------------------------------------------------------------------------------------------------------------

# How I Created My YAML (CI/CD Workflow)

First, I made sure that my tests were working correctly by running pytest locally. Once everything passed, I created Docker configurations for both the frontend and backend, and pushed the project to GitHub.
Second, after everything was in place on GitHub, I went to the “Actions” tab. GitHub suggested workflow templates based on my project.
Third, I selected the “Docker image” workflow template. GitHub automatically generated a workflow file located at:

.github/workflows/docker-image.yml

I then renamed this file to ci.yml to better match my project.
This generated file provided a ready-made structure, so I didn’t need to write the YAML from scratch. I copied this workflow into my local project in VS Code under:

.github/workflows/ci.yml

Next, I edited the YAML file to fit my project requirements (such as adding test steps, Docker build, and push configuration).
How I Found the Right Template
To explore more templates, I went to GitHub Actions workflows and searched for Python. I found the “Build and test Python” template, which helped me understand how to structure testing steps in my pipeline.


--------------------------------------------------------------------------------------------------------------------------------------------------------


When creating a second pipeline to train the model, I had to update my code in train.py.

At first, I was using:

df = pd.read_csv("../../datas/Iris.csv")

This worked only in my local environment because the relative path depended on where I launched the script.

To make the code work both locally and inside the pipeline, I changed it to use os.path.dirname() and os.path.join() so the dataset path is built dynamically based on the file location.

For example:

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datas", "Iris.csv")

df = pd.read_csv(DATA_PATH)

This approach is more reliable because it does not depend on the current working directory.

I also had to remove mlflow.db from the second pipeline, because it should not be reused or committed as a fixed local file in the workflow environment.