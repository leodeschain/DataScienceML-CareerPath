# Exemplo de script de treinamento de modelo.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib
import json

# Carregar configuração do experimento
with open('30_ML_CORE/experiments/exp_001_classification/config.json') as f:
    config = json.load(f)

# Carregar dados
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Preparar dados
X = df[config['features']]
y = df[config['target']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=config['parameters']['random_state'])

# Treinar modelo
model = RandomForestClassifier(
    n_estimators=config['parameters']['n_estimators'],
    max_depth=config['parameters']['max_depth'],
    random_state=config['parameters']['random_state']
)
model.fit(X_train, y_train)

# Salvar modelo
model_filename = f"30_ML_CORE/models/{config['experiment_name']}.joblib"
joblib.dump(model, model_filename)

print(f"Modelo treinado e salvo em: {model_filename}")
print(f"Acurácia no set de teste: {model.score(X_test, y_test)}")
