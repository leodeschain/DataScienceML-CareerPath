# Análise Exploratória de Dados (EDA) - Dataset Iris

**Objetivo:** Explorar o dataset Iris para entender suas características, a distribuição das variáveis e as relações entre elas. Esta análise é fundamental para extrair insights e preparar os dados para a modelagem.
# Importação das bibliotecas essenciais
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Configuração para os plots
sns.set_theme(style="whitegrid")
## 1. Carregamento dos Dados

Vamos carregar o dataset Iris diretamente da biblioteca `scikit-learn` e convertê-lo para um DataFrame do pandas, que é mais fácil de manipular.
# Carrega o dataset
iris = load_iris()

# Cria o DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Mapeia os números do target para os nomes das espécies
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species_name'] = df['species'].map(species_map)

print("Dataset carregado com sucesso!")
## 2. Inspeção Inicial dos Dados

Vamos verificar as primeiras linhas, os tipos de dados e se há valores nulos.
# Exibe as 5 primeiras linhas
df.head()
# Exibe informações sobre o DataFrame (tipos, valores não-nulos)
df.info()
## 3. Estatística Descritiva

Resumo estatístico para entender a tendência central, dispersão e formato da distribuição de cada variável numérica.
df.describe()
## 4. Visualização dos Dados

Agora, vamos criar gráficos para visualizar as distribuições e relações.

### Pair Plot
Um `pairplot` mostra a relação entre cada par de variáveis e a distribuição de cada uma na diagonal. É excelente para uma visão geral rápida.
# O 'hue' colore os pontos de acordo com a espécie da flor
sns.pairplot(df.drop('species', axis=1), hue='species_name', palette='viridis', diag_kind='kde')