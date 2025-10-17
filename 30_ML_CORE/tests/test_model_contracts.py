import pytest
import joblib
import pandas as pd
import numpy as np

# Supondo que um modelo treinado exista em ../models/
MODEL_PATH = "../models/classification_iris.joblib" 

@pytest.fixture
def model():
    """Carrega o modelo treinado."""
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        pytest.skip(f"Modelo não encontrado em {MODEL_PATH}. Pule o teste.")

def test_model_prediction_output(model):
    """
    Testa o tipo e o formato da saída da predição do modelo.
    """
    # Criar dados de exemplo com o formato esperado
    sample_data = pd.DataFrame(np.random.rand(10, 4), columns=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ])
    
    predictions = model.predict(sample_data)
    
    # A saída deve ser um array numpy
    assert isinstance(predictions, np.ndarray)
    
    # A saída deve ter o mesmo número de predições que a entrada
    assert len(predictions) == 10
    
    # Os valores preditos devem ser inteiros (classes)
    assert all(isinstance(p, np.integer) for p in predictions)

def test_model_expected_features(model):
    """
    Testa se o modelo foi treinado com as features esperadas.
    """
    expected_features = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ]
    # Para modelos scikit-learn, as features estão em `feature_names_in_`
    assert hasattr(model, 'feature_names_in_')
    assert list(model.feature_names_in_) == expected_features
