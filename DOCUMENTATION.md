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

#### to train the model 


#### for the backend 

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






--------------------------------------------------------------


HOw I created my yaml ?
First, I make sure that my test work when i did pytest that it works... did my docker for the frontend and backend then I pushed it into Github. 
Second, when everythings in place in the github. Clicked on the " actions " then you will suggested repository for you rproject. 
Third, configure " docker image". 
From here you will see it will generate a folder /.github/workflows/docker-image.yml (you can change the name and i did chaned mine to ci.yml) in main.
It automated the code inside the docker-image.yml and now I can use and edit it. No need to do it in scratch.
Copy how the folder has been created and put it in VScode /.github/workflows/ci.yml
Next, paste the code  on my vscode and edit it. 



To check for the template 
go to github action workflow 
since i am using python i did search python then you will see "building and testing python" click on it



----------
for the marketplace of github action of docker build and push sample template https://github.com/marketplace/actions/docker-build-push-action 





---------------------------------- -------
when creating a second pipeline to train the model i have to change my code from 
train.py 
df = pd.read_csv("../../datas/Iris.csv")    this code only work in local 

to 

os.path.dirname(path, /)
Return the directory name of pathname path. This is the first element of the pair returned by passing path to the function split().

have to remove mlflow.db for the 2nd pipeline 