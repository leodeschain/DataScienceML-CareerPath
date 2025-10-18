import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Classificador de Íris", layout="wide")

# Título
st.title("Classificador de Flor de Íris")

# Carregar o modelo
@st.cache_resource
def load_model():
    try:
        return joblib.load("30_ML_CORE/models/classification_iris.joblib")
    except FileNotFoundError:
        return None

model = load_model()

if model is None:
    st.error("Modelo não encontrado. Por favor, treine o modelo primeiro (`30_ML_CORE/training/train.py`).")
else:
    st.success("Modelo carregado com sucesso!")

    # Sidebar para entrada de dados do usuário
    st.sidebar.header("Insira as Características da Flor:")

    def user_input_features():
        sepal_length = st.sidebar.slider('Comprimento da Sépala (cm)', 4.0, 8.0, 5.4)
        sepal_width = st.sidebar.slider('Largura da Sépala (cm)', 2.0, 4.5, 3.4)
        petal_length = st.sidebar.slider('Comprimento da Pétala (cm)', 1.0, 7.0, 1.6)
        petal_width = st.sidebar.slider('Largura da Pétala (cm)', 0.1, 2.5, 0.4)
        data = {
            'Comprimento da Sépala': sepal_length,
            'Largura da Sépala': sepal_width,
            'Comprimento da Pétala': petal_length,
            'Largura da Pétala': petal_width
        }
        features = pd.DataFrame(data, index=[0])
        return features

    df_input = user_input_features()

    # Mostrar os dados de entrada
    st.subheader("Características Inseridas:")
    st.write(df_input)

    # Fazer a predição
    if st.button("Classificar"):
        prediction = model.predict(df_input.values)
        prediction_proba = model.predict_proba(df_input.values)
        
        target_names = ['Setosa', 'Versicolor', 'Virginica']
        
        st.subheader("Resultado da Classificação:")
        st.write(f"**Espécie Prevista:** {target_names[prediction[0]]}")
        
        st.subheader("Probabilidades:")
        df_proba = pd.DataFrame(prediction_proba, columns=target_names)
        st.write(df_proba)
