# About the Project

As part of this project, our teacher Bob challenged us to build the solution without relying on Large Language Models (LLMs).

Instead, the focus was on:

understanding the concepts
writing the code independently
solving problems through practice and collaboration

This approach helped strengthen my fundamentals in machine learning and software development.

### Objective 
The goal of this project is to:

Train a machine learning model on the Iris dataset
Serve predictions through an API
Containerize the application (backend & frontend)
Automate testing and deployment with CI/CD

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
--------------------------------------------------------------------------------------------------------------------------
# Acknowledgment

This project was developed as part of the Simplon AI Developer training program.

I completed this project by focusing on hands-on learning and problem-solving.
There were challenges along the way, but collaboration with my teammates (YassGPT, LiliGPT and AhmGPT) helped me successfully complete the project.