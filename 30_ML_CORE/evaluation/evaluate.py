# Exemplo de script de avaliação de modelo.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
import joblib
import json

# Carregar configuração do experimento
with open('../experiments/exp_001_classification/config.json') as f:
    config = json.load(f)

# Carregar modelo
model_filename = f"../models/{config['experiment_name']}.joblib"
model = joblib.load(model_filename)

# Carregar dados
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
X = df[config['features']]
y = df[config['target']]
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=config['parameters']['random_state'])

# Fazer predições
y_pred = model.predict(X_test)

# Gerar relatório de classificação
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print("Relatório de Classificação:")
print(report)

# Salvar métricas (exemplo)
report_dict = classification_report(y_test, y_pred, output_dict=True)
metrics_filename = f"../models/{config['experiment_name']}_metrics.json"
with open(metrics_filename, 'w') as f:
    json.dump(report_dict, f, indent=4)

print(f"Métricas salvas em: {metrics_filename}")
