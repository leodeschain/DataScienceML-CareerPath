import requests
import json

# URL da sua API FastAPI rodando localmente
url = "http://127.0.0.1:8000/predict/"

# Dados de exemplo para uma flor de íris
# (setosa, versicolor, virginica)
payloads = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}, # setosa
    {"sepal_length": 6.7, "sepal_width": 3.1, "petal_length": 4.7, "petal_width": 1.5}, # versicolor
    {"sepal_length": 6.3, "sepal_width": 2.9, "petal_length": 5.6, "petal_width": 1.8}  # virginica
]

for payload in payloads:
    try:
        response = requests.post(url, data=json.dumps(payload))
        response.raise_for_status()
        
        print(f"Enviando dados: {payload}")
        print(f"Resposta da API: {response.json()}")
        print("-" * 30)
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
