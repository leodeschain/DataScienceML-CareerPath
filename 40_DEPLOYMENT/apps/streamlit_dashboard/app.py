import streamlit as st
import pandas as pd
import joblib
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Classificador de Íris", layout="wide")

# Título
st.title("Classificador de Flor de Íris")

# Define o diretório raiz do projeto dinamicamente
# O script está em '40_DEPLOYMENT/apps/streamlit_dashboard/', então subimos 4 níveis para chegar na raiz
PROJETO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
MODEL_PATH = PROJETO_ROOT / "30_ML_CORE" / "models" / "classification_iris.joblib"

# Carregar o modelo
@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        return None

model = load_model()

if model is None:
    st.error(f"Modelo não encontrado em: {MODEL_PATH}. Por favor, treine o modelo primeiro executando '30_ML_CORE/training/train.py'.")
else:
    st.success("Modelo carregado com sucesso!")

    # Sidebar para entrada de dados do usuário
    st.sidebar.header("Insira as Características da Flor:")

    def user_input_features():
        sepal_length = st.sidebar.slider('Comprimento da Sépala (cm)', 4.0, 8.0, 5.4)
        sepal_width = st.sidebar.slider('Largura da Sépala (cm)', 2.0, 4.5, 3.4)
        petal_length = st.sidebar.slider('Comprimento da Pétala (cm)', 1.0, 7.0, 1.6)
        petal_width = st.sidebar.slider('Largura da Pétala (cm)', 0.1, 2.5, 0.4)
        
        # As colunas do DataFrame de input devem corresponder exatamente às features do modelo
        # O modelo foi treinado com: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
        input_data = {
            "sepal length (cm)": sepal_length,
            "sepal width (cm)": sepal_width,
            "petal length (cm)": petal_length,
            "petal width (cm)": petal_width
        }
        
        features = pd.DataFrame(input_data, index=[0])
        return features

    df_input = user_input_features()

    # Mostrar os dados de entrada
    st.subheader("Características Inseridas:")
    st.write(df_input)

    # Fazer a predição
    if st.button("Classificar"):
        # Passamos o DataFrame diretamente, pois as colunas já estão na ordem correta
        prediction = model.predict(df_input)
        prediction_proba = model.predict_proba(df_input)
        
        target_names = ['Setosa', 'Versicolor', 'Virginica']
        
        st.subheader("Resultado da Classificação:")
        st.write(f"**Espécie Prevista:** {target_names[prediction[0]]}")
        
        st.subheader("Probabilidades:")
        df_proba = pd.DataFrame(prediction_proba, columns=target_names)
        st.write(df_proba)


st.info("Este é um aplicativo de exemplo para demonstrar a classificação de flores de Íris com um modelo de Machine Learning treinado.")
st.markdown("---")
st.markdown("Desenvolvido como parte do portfólio de Data Science & ML.")

