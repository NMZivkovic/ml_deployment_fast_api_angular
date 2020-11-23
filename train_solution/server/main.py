from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_trainer import ModelTrainer
from train_parameters import TrainParameters
from penguin_sample import PenguinSample

origins = [
    "http://localhost:8000",
    "http://localhost:4200"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.model = ModelTrainer('svm')

@app.post("/train")
async def train(params: TrainParameters):
    print("Model Training Started")
    app.model =  ModelTrainer(params.model.lower(), params.testsize)
    accuracy = app.model.train(params.path)
    return accuracy

@app.post("/predict")
async def predict(data:PenguinSample):
    print("Predicting")
    spicies_map = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}
    species = app.model.predict(data)
    return spicies_map[species[0]]