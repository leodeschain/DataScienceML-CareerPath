# Exemplo de script de treinamento de modelo.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib
import json
from pathlib import Path

def main():
    """Função principal para treinar o modelo."""
    # Define o diretório raiz do projeto dinamicamente
    # O script está em '30_ML_CORE/training/', então subimos 3 níveis
    PROJETO_ROOT = Path(__file__).resolve().parent.parent.parent

    # Caminhos para os arquivos, construídos a partir da raiz do projeto
    config_path = PROJETO_ROOT / "30_ML_CORE" / "experiments" / "exp_001_classification" / "config.json"
    model_dir = PROJETO_ROOT / "30_ML_CORE" / "models"

    # Garante que o diretório de modelos exista
    model_dir.mkdir(exist_ok=True)

    # Carregar configuração do experimento
    with open(config_path) as f:
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
    model_filename = model_dir / f"{config['experiment_name']}.joblib"
    joblib.dump(model, model_filename)

    print(f"Modelo treinado e salvo em: {model_filename}")
    print(f"Acurácia no set de teste: {model.score(X_test, y_test)}")

if __name__ == "__main__":
    main()
