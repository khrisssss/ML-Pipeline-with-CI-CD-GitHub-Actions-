This is a simple project with MLFlow to train the dataset of iris flowers using logisticregression.

We the students, trained the data to predict 3 kind of variety of iris flowers using the sepals and petals length and width (in cm).
In this project I did not use LLM at all.


# Project Structure 
ml_pipeline/
├── backend/                         
│   ├── app/
│   │   └── app_api.py               # Flask API 
│   │
│   ├── ml/
│   │   ├── train_notebook.ipynb     # Jupyter notebook used for exploration to check the data
│   │   └── train.py
│   │
│   ├── test/
│   │   └── test_predict.py
│   │
│   └── Dockerfile
│   
├── frontend/
│   ├── app
│   └── Dockerfile      
│                
├── .gitignore                
│                   
└──  DOCUMENTATION.md           

# Launching in local 

##### for the backend 

''' bash 
#backend/app
uvicorn app_api:app 
'''

#### for the frontend

''' bash 
#frontend/app
streamlit run app.py
'''

# test 
Wen you do a test if the connection is correct make sure you are just in the folder of ml_pipeline then run 
''' bash 
pytest
'''
If you see i collected an item and its not failed then connection is good



#### to build the imahe of backend docker file
''' bash 
#ml_pipeline/backend
docker build --no-cache -t backend .
'''  



