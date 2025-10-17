from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Carregar o modelo
try:
    model = joblib.load("../../models/classification_iris.joblib")
except FileNotFoundError:
    model = None

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "API de Classificação de Íris"}

@app.post("/predict/")
def predict_iris(features: IrisFeatures):
    if model is None:
        return {"error": "Modelo não encontrado. Treine o modelo primeiro."}
        
    data = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])
    
    prediction = model.predict(data)
    prediction_proba = model.predict_proba(data).tolist()
    
    # Nomes das classes do Iris
    target_names = ['setosa', 'versicolor', 'virginica']
    
    return {
        "prediction": target_names[prediction[0]],
        "prediction_label": int(prediction[0]),
        "probabilities": dict(zip(target_names, prediction_proba[0]))
    }
